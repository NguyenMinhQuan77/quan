import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Python"

# đếm xem có bao nhiêu ảnh bằng requests và BeautifulSoup, in ra url của ảnh

headers = requests.utils.default_headers()
response = requests.get(url, headers)


soup = BeautifulSoup(response.content, "html.parser")

images = soup.find_all("img")
print("Number of images:", len(images))

for image in images:
    print(image["src"])
