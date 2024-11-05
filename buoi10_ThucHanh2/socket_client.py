import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 1234))

    while True:
        # Nhập chuỗi từ người dùng
        data = input("Nhập xâu bất kỳ (hoặc 'exit' để thoát): ")
        if data == 'exit':
            break

        # Gửi dữ liệu lên server
        s.send(data.encode("utf-8"))

        # Nhận kết quả từ server
        result = s.recv(1024).decode("utf-8")
        print(f"Chuỗi chuẩn hóa từ server: {result}")

    s.close()
