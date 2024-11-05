import socket

if __name__ == '__main__':
    # Khởi tạo socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Kết nối tới server
    s.connect(('127.0.0.1', 1234))
    print("Đã kết nối tới server")

    while True:
        # Nhập mã sinh viên từ bàn phím
        masv = input("Nhập mã sinh viên cần tìm (nhập 'exit' để thoát): ")
        if masv.lower() == 'exit':
            break

        # Gửi Masv lên server
        s.send(masv.encode("utf-8"))

        # Nhận kết quả từ server
        result = s.recv(1024).decode("utf-8")
        print(f"Kết quả từ server: {result}")

    s.close()
