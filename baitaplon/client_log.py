import socket
import os

# Địa chỉ server
HOST = '127.0.0.1'  # localhost
PORT = 65432  # Port để kết nối

# Hàm tải lên file
def upload_file(conn):
    filename = input("Enter the filename to upload: ")
    if not os.path.isfile(filename):
        print("File not found. Please check the filename and try again.")
        return

    conn.sendall(b"UPLOAD")
    conn.sendall(filename.encode())

    with open(filename, "rb") as f:
        data = f.read(1024)
        while data:
            conn.send(data)
            data = f.read(1024)
    print("File uploaded successfully.")

# Hàm tải xuống file
def download_file(conn):
    filename = input("Enter the filename to download: ")
    conn.sendall(b"DOWNLOAD")
    conn.sendall(filename.encode())

    response = conn.recv(1024).decode()
    if response == "EXISTS":
        with open("downloaded_" + filename, "wb") as f:
            data = conn.recv(1024)
            while data:
                f.write(data)
                if len(data) < 1024:
                    break
                data = conn.recv(1024)
        print("File downloaded successfully.")
    elif response == "NOT FOUND":
        print("File not found on server.")

# Hàm chính của client
def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(username.encode())
        s.sendall(password.encode())

        response = s.recv(1024).decode()
        print(response)

        if response == "Login successful":
            while True:
                action = input("Enter 'upload', 'download', or 'exit': ").strip().lower()
                if action == "upload":
                    upload_file(s)
                elif action == "download":
                    download_file(s)
                elif action == "exit":
                    s.sendall(b"EXIT")
                    print("Exiting client.")
                    break
                else:
                    print("Invalid action. Please try again.")
        else:
            print("Login failed. Please check your username and password.")

if __name__ == "__main__":
    main()
