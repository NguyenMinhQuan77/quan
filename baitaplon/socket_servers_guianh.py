import socket
import cv2
import pickle
import struct

# Tạo socket và lắng nghe kết nối
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '127.0.0.1'  # Địa chỉ IP của máy
port = 9999
server_socket.bind((host_ip, port))
server_socket.listen(5)
print("Server is listening...")

while True:
    conn, addr = server_socket.accept()
    print('Got connection from', addr)

    while True:
        # Nhận dữ liệu hình ảnh từ client
        data = b""
        payload_size = struct.calcsize("Q")
        while len(data) < payload_size:
            packet = conn.recv(4 * 1024)  # 4K
            if not packet:
                break
            data += packet

        if not data:
            break

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]
        while len(data) < msg_size:
            data += conn.recv(4 * 1024)
        frame_data = data[:msg_size]
        data = data[msg_size:]

        # Giải mã và hiển thị frame
        frame = pickle.loads(frame_data)
        cv2.imshow('SERVERS VIDEO', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    conn.close()

server_socket.close()
