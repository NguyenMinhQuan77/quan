import socket
import cv2
import pickle
import struct

# Kết nối đến server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '127.0.0.1'  # Địa chỉ IP của server
port = 9999
client_socket.connect((host_ip, port))

# Bắt đầu capture video từ webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Chuyển đổi frame thành dữ liệu để gửi
    data = pickle.dumps(frame)
    message = struct.pack("Q", len(data)) + data
    client_socket.sendall(message)

    # Hiển thị video
    cv2.imshow('ClIENT VIDEO', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
client_socket.close()
cv2.destroyAllWindows()
