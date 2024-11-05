import socket

# CSDL sinh viên: Masv, Hoten, DTB
csdl_sv = {
    "001": {"Hoten": "Nguyen Van A", "DTB": 7.5},
    "002": {"Hoten": "Le Thi B", "DTB": 8.0},
    "003": {"Hoten": "Tran Van C", "DTB": 6.8},
}

def tim_kiem_sv(masv):
    # Tìm sinh viên theo Masv
    if masv in csdl_sv:
        sv = csdl_sv[masv]
        return f"Masv: {masv}, Hoten: {sv['Hoten']}, DTB: {sv['DTB']}"
    else:
        return "Không có"

if __name__ == '__main__':
    # Khởi tạo socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 1234))  # Địa chỉ IP và port của server
    s.listen(5)
    print("Server đang chờ kết nối...")

    # Chấp nhận kết nối từ client
    client_sk, client_addr = s.accept()
    print(f"Client {client_addr} đã kết nối")

    while True:
        # Nhận dữ liệu từ client
        masv = client_sk.recv(1024).decode("utf-8")
        if not masv:
            break
        print(f"Nhận từ client Masv: {masv}")

        # Tìm kiếm sinh viên
        result = tim_kiem_sv(masv)
        print(f"Kết quả tìm kiếm: {result}")

        # Gửi kết quả về client
        client_sk.send(result.encode("utf-8"))

    client_sk.close()
    s.close()
