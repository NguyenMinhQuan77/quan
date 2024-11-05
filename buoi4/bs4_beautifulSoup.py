import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://en.wikipedia.org/wiki/Python")

bs = BeautifulSoup(url, "html.parser")

# for link in bs.find_all("a"):
#     if "href" in link.attrs:
#         print(link.attrs["href"])

# count number of images in url

images = bs.find_all("img")
print("Number of images:", len(images))

