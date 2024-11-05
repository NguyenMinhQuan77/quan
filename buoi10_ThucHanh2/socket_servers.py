import socket


# Hàm chuẩn hóa chuỗi
# Hàm chuẩn hóa chuỗi
def chuan_hoa_xau(s):
    # Loại bỏ khoảng trắng thừa
    s = ' '.join(s.split())

    # Chuẩn hóa khoảng trắng sau dấu chấm, dấu phẩy
    s = s.replace(' ,', ',').replace(' .', '.').replace(',', ', ').replace('.', '. ')

    # Xử lý viết hoa ký tự đầu tiên của xâu và ký tự đầu sau dấu chấm
    s = s.strip()
    s = s.capitalize()

    # Viết hoa chữ cái sau dấu chấm
    new_s = ''
    capitalize_next = False
    for i in range(len(s)):
        if capitalize_next and s[i].isalpha():
            new_s += s[i].upper()
            capitalize_next = False
        else:
            new_s += s[i]
        if s[i] == '.':
            capitalize_next = True

    # Thêm dấu chấm cuối câu nếu chưa có
    if not new_s.endswith('.'):
        new_s += '.'

    return new_s



if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #giao thúc TCP
    s.bind(('127.0.0.1', 1234))
    s.listen(5)
    print("Server đang chờ kết nối...")

    client_sk, client_addr = s.accept()
    print(f"Client {client_addr} đã kết nối")

    while True:
        # Nhận dữ liệu từ client
        data = client_sk.recv(1024).decode("utf-8")
        if not data:
            break
        print(f"Nhận từ client: {data}")

        # Chuẩn hóa chuỗi
        result = chuan_hoa_xau(data)
        print(f"Chuỗi đã chuẩn hóa: {result}")

        # Gửi chuỗi đã chuẩn hóa về client
        client_sk.send(result.encode("utf-8"))

    client_sk.close()
    s.close()
