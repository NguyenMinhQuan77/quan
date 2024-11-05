import requests
import getpass

link = "https://sis.utc.edu.vn"
url = "https://sis.utc.edu.vn/survey/overview.php"

# username = input("Enter your username: ")
# password = getpass.getpass("Enter your password: ")

data = {
    "username": "quan211200891@lms.utc.edu.vn",
    "password": "0963943984q"
}

# đăng nhập vào link

response = requests.post(link, data=data)

if response.status_code == 200:
    print("Login successful")
else:
    print("Login failed")

# get request

response = requests.get(url)
print("status code", response.status_code)
print("Body", response.text)


# lấy dữ liệu từ url