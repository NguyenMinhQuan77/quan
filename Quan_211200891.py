import ftplib  # Thư viện để làm việc với giao thức FTP
import os  # Thư viện để làm việc với hệ thống tệp

# Hàm liệt kê thư mục


def list_directory(ftp):
    print("---------- Function list_directory ----------")
    try:
        files = []  # Danh sách để lưu các tệp
        ftp.dir(files.append)  # Lấy danh sách tệp và thêm vào danh sách
        return files  # Trả về danh sách tệp
    except ftplib.all_errors as e:
        print(f"Error listing directory: {e}")  # In ra lỗi nếu có
        return []  # Trả về danh sách rỗng nếu có lỗi

# Hàm tải tệp xuống

def download_file(ftp, file_orig, file_copy):
    print("---------- Function download_file ----------")
    try:
        with open(file_copy, "wb") as fp:  # Mở tệp để ghi dữ liệu nhị phân
            ftp.retrbinary("RETR " + file_orig, fp.write)  # Tải tệp xuống
        # In ra thông báo tải thành công
        print(
            f"Download of {file_orig} to {file_copy} completed successfully.")
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")  # In ra lỗi nếu có
        if os.path.isfile(file_copy):  # Nếu tệp đã tồn tại
            os.remove(file_copy)  # Xóa tệp

# Hàm tải tệp lên
def upload_file(ftp, filename):
    print("---------- Function upload_file ----------")
    try:
        with open(filename, "rb") as fp:  # Mở tệp để đọc dữ liệu nhị phân
            res = ftp.storbinary("STOR " + filename, fp)  # Tải tệp lên
            print(f"Server response: {res}")  # In ra phản hồi từ máy chủ
            if not res.startswith("226"):  # Nếu phản hồi không bắt đầu bằng "226"
                print("Upload failed")  # In ra thông báo tải lên thất bại
            else:
                # In ra thông báo tải lên thành công
                print(f"Upload of {filename} completed successfully.")
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")  # In ra lỗi nếu có

# Hàm đổi tên tệp hoặc thư mục

def rename_file_or_directory(ftp, from_name, to_name):
    print("---------- Function rename_file_or_directory ----------")
    try:
        ftp.rename(from_name, to_name)  # Đổi tên tệp hoặc thư mục
        # In ra thông báo đổi tên thành công
        print(f"Renamed {from_name} to {to_name}")
    except ftplib.all_errors as e:
        # In ra lỗi nếu có
        print(f"Error renaming {from_name} to {to_name}: {e}")

# Hàm xóa tệp

def delete_file(ftp, filename):
    print("---------- Function delete_file ----------")
    try:
        ftp.delete(filename)  # Xóa tệp
        print(f"Deleted file: {filename}")  # In ra thông báo xóa thành công
    except ftplib.all_errors as e:
        print(f"Error deleting file: {e}")  # In ra lỗi nếu có


# Hàm tạo thư mục

def create_directory(ftp, directory):
    print("---------- Function create_directory ----------")
    try:
        ftp.mkd(directory)  # Tạo thư mục
        # In ra thông báo tạo thành công
        print(f"Created directory: {directory}")
    except ftplib.all_errors as e:
        print(f"Error creating directory: {e}")  # In ra lỗi nếu có



# Hàm in menu
def print_menu():
    print("\nMenu:")
    print("1. List directory")  # Liệt kê thư mục
    print("2. Download file")  # Tải tệp xuống
    print("3. Upload file")  # Tải tệp lên
    print("4. Rename file or directory")  # Đổi tên tệp hoặc thư mục
    print("5. Delete file")  # Xóa tệp
    print("6. Create directory")  # Tạo thư mục
    print("7. Exit")  # Thoát



# Chương trình chính
if __name__ == "__main__":
    with ftplib.FTP("127.0.0.1") as ftp:  # Kết nối tới máy chủ FTP
        try:
            username = input("Nhập tên người dùng FTP: ").strip();
            password = input("Nhập mật khẩu FTP: ").strip();
            ftp.login(username, password);
            ftp.set_pasv(True)  # Bật chế độ truyền dữ liệu thụ động

            # test kết nối thành công
            print(ftp.getwelcome())  # In ra thông báo chào mừng từ máy chủ

            while True:
                print_menu()  # In menu
                choice = input("Enter your choice: ")  # Nhập lựa chọn

                if choice == "1":
                    entries = list_directory(ftp)  # Liệt kê thư mục
                    print(len(entries), "entries:")  # In ra số lượng tệp
                    for entry in entries:
                        print(entry)  # In ra từng tệp

                elif choice == "2":
                    # Nhập tên tệp từ xa cần tải xuống
                    file_orig = input("Enter remote filename to download: ")
                    # Nhập đường dẫn và tên tệp để lưu
                    file_copy = input(
                        "Enter local path and filename to save as: ")
                    download_file(ftp, file_orig, file_copy)  # Tải tệp xuống

                elif choice == "3":
                    # Nhập tên tệp cần tải lên
                    filename = input("Enter local filename to upload: ")
                    upload_file(ftp, filename)  # Tải tệp lên

                elif choice == "4":
                    # Nhập tên hiện tại
                    from_name = input("Enter current name: ")
                    to_name = input("Enter new name: ")  # Nhập tên mới
                    # Đổi tên tệp hoặc thư mục
                    rename_file_or_directory(ftp, from_name, to_name)


                elif choice == "5":
                    # Nhập tên tệp cần xóa
                    filename = input("Enter filename to delete: ")
                    delete_file(ftp, filename)  # Xóa tệp

                elif choice == "6":
                    # Nhập tên thư mục cần tạo
                    directory = input("Enter directory name to create: ")
                    create_directory(ftp, directory)  # Tạo thư mục

                elif choice == "7":
                    print("Exiting...")  # In ra thông báo thoát
                    break  # Thoát khỏi vòng lặp

                else:
                    # In ra thông báo lựa chọn không hợp lệ
                    print("Invalid choice. Please try again.")

        except ftplib.all_errors as e:
            print(f"FTP error: {e}")  # In ra lỗi nếu có
