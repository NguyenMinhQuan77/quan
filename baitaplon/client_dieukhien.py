import socket
import cv2
import numpy as np
import pickle
import struct
import pyautogui
import os
import time

# Thiết lập socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '127.0.0.1'  # Địa chỉ IP của server
port = 9999
client_socket.connect((host_ip, port))

try:
    while True:
        # Chụp màn hình
        screenshot = pyautogui.screenshot()

        # Kiểm tra kích thước screenshot
        if screenshot is not None:
            print("Screenshot taken successfully.")
        else:
            print("Failed to take screenshot.")

        # Chuyển đổi screenshot thành frame OpenCV
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Kiểm tra kích thước frame
        print(f"Frame size: {frame.shape}")  # In kích thước của frame

        # Chuyển đổi frame thành dữ liệu để gửi
        data = pickle.dumps(frame)
        message = struct.pack("Q", len(data)) + data
        client_socket.sendall(message)

        # Nhận và xử lý lệnh từ server
        command = client_socket.recv(1024).decode()

        if command == "move_mouse":
            position = client_socket.recv(1024).decode()
            x, y = map(int, position.split())
            pyautogui.moveTo(x, y)

        elif command == "type_text":
            text = client_socket.recv(1024).decode()
            pyautogui.write(text)

        elif command == "system_command":
            sys_cmd = client_socket.recv(1024).decode()
            os.system(sys_cmd)

        elif command == "exit":
            break

        # Hiển thị frame để xác minh
        cv2.imshow("Sending Screen", frame)

        # Đợi một khoảng thời gian nhỏ để không gửi quá nhiều dữ liệu liên tiếp
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Client disconnected.")

finally:
    client_socket.close()
    cv2.destroyAllWindows()
