import requests
from bs4 import BeautifulSoup

url = "https://forecast.weather.gov/MapClick.php?lat=42.93708397900008&lon=-75.61070144699994"

response = requests.get(url)
print(response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Lấy thông tin thời tiết
    week = soup.find(id="seven-day-forecast")
    w = week.find_all(class_="tombstone-container")
    d = []
    for i in w:
        day = i.find(class_="period-name").get_text()
        desc = i.find(class_="short-desc").get_text()
        temp = i.find(class_="temp").get_text()
        img = i.find("img")["title"]
        d.append((day, desc, temp, img))

    # in vào file output.txt
    with open("output.txt", "w") as file:
        for i in d:
            file.write(f"{i[0]}: {i[1]}, {i[2]}, {i[3]}\n")

else:
    print("Không thể kết nối đến trang web") 


