import socket
import cv2
import pickle
import struct

# Thiết lập socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '0.0.0.0'  # Chấp nhận tất cả các địa chỉ IP
port = 9999
server_socket.bind((host_ip, port))
server_socket.listen(5)
print("Server is listening...")

# Chờ client kết nối
conn, addr = server_socket.accept()
print(f"Connected to: {addr}")

try:
    while True:
        # Nhận và hiển thị màn hình từ client
        data = b""
        payload_size = struct.calcsize("Q")

        while len(data) < payload_size:
            packet = conn.recv(4 * 1024)  # Nhận tối đa 4KB
            if not packet:
                break
            data += packet

        if len(data) < payload_size:
            break

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            data += conn.recv(4 * 1024)

        frame_data = data[:msg_size]

        # Kiểm tra kích thước khung hình
        if len(frame_data) < msg_size:
            print("Lỗi: Kích thước khung hình không hợp lệ")
            continue

        frame = pickle.loads(frame_data)

        # Kiểm tra kích thước và điều chỉnh nếu cần
        height, width, channels = frame.shape
        if height > 600 or width > 800:
            frame = cv2.resize(frame, (800, 600))

        cv2.imshow("Remote Screen", frame)
        cv2.waitKey(1)  # Thêm dòng này để cập nhật cửa sổ hiển thị

        # Hiển thị menu lệnh
        print("\n--- Command Menu ---")
        print("Nhập 'move_mouse': Di chuyển chuột trên máy client.")
        print("Nhập 'type_text': Nhập nội dung muốn gõ trên máy client.")
        print("Nhập 'system_command': Thực thi lệnh hệ thống trên máy client (ví dụ: notepad).")
        print("Nhập 'exit': Dừng chương trình.")

        command = input("Enter command: ")

        if command == "move_mouse":
            conn.sendall(command.encode())
            position = input("Enter x y coordinates (e.g., 200 200): ")
            conn.sendall(position.encode())
            print(f"Command '{command}' sent with position {position}.")

        elif command == "type_text":
            conn.sendall(command.encode())
            text = input("Enter text to type: ")
            conn.sendall(text.encode())
            print(f"Command '{command}' sent with text '{text}'.")

        elif command == "system_command":
            conn.sendall(command.encode())
            sys_cmd = input("Enter system command to execute: ")
            conn.sendall(sys_cmd.encode())
            print(f"Command '{command}' sent with system command '{sys_cmd}'.")

        elif command == "exit":
            conn.sendall(command.encode())
            print("Exiting program.")
            break

        # Kiểm tra phím để thoát
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"Lỗi: {str(e)}")

finally:
    conn.close()
    server_socket.close()
    cv2.destroyAllWindows()
