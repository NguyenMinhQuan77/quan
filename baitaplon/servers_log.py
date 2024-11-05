import socket
import threading
import os
from datetime import datetime

# Địa chỉ server
HOST = '127.0.0.1'  # localhost
PORT = 65432  # Port để kết nối

# Danh sách tài khoản
users = {
    "u": "p",
    "u2": "p2"
}

# Thư mục lưu trữ file
FILE_DIRECTORY = "shared_files"

# Tạo thư mục nếu chưa tồn tại
if not os.path.exists(FILE_DIRECTORY):
    os.makedirs(FILE_DIRECTORY)


# Hàm ghi nhật ký
def log_activity(action, filename, username):
    with open("activity_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {action} - {filename} by {username}\n")


# Hàm xử lý client
def handle_client(conn, addr):
    print(f"Connected by {addr}")
    username = conn.recv(1024).decode()
    password = conn.recv(1024).decode()

    # Kiểm tra thông tin đăng nhập
    if username in users and users[username] == password:
        conn.sendall(b"Login successful")
        print(f"User '{username}' logged in.")
    else:
        conn.sendall(b"Login failed")
        print(f"Failed login attempt for user '{username}'.")
        conn.close()
        return

    while True:
        command = conn.recv(1024).decode()
        print(f"Received command: {command} from {username}")

        if command == "UPLOAD":
            filename = conn.recv(1024).decode()
            filepath = os.path.join(FILE_DIRECTORY, filename)
            print(f"Receiving upload: {filename} from {username}")
            with open(filepath, "wb") as f:
                data = conn.recv(1024)
                while data:
                    f.write(data)
                    data = conn.recv(1024)
            log_activity("UPLOAD", filename, username)
            conn.sendall(b"Upload successful")

        elif command == "DOWNLOAD":
            filename = conn.recv(1024).decode()
            filepath = os.path.join(FILE_DIRECTORY, filename)
            if os.path.isfile(filepath):
                print(f"Sending file: {filename} to {username}")
                conn.sendall(b"EXISTS")
                with open(filepath, "rb") as f:
                    data = f.read(1024)
                    while data:
                        conn.send(data)
                        data = f.read(1024)
                log_activity("DOWNLOAD", filename, username)
                conn.sendall(b"Done")
            else:
                print(f"File not found: {filename} requested by {username}")
                conn.sendall(b"NOT FOUND")

        elif command == "EXIT":
            print(f"User '{username}' disconnected.")
            conn.close()
            break


# Hàm chạy server
def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Server is listening...")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()


if __name__ == "__main__":
    run_server()

