from urllib.request import urlopen
from urllib.request import Request
from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor
import datetime

if __name__ == '__main__':
    cj = CookieJar()
    opener = build_opener(HTTPCookieProcessor(cj))
    r = Request('http://github.com')
    r1 = opener.open(r)  # Mở URL và nhận phản hồi

    print(len(cj))
    cookies = list(cj)

    if len(cookies) > 1:
        print(cookies[1].name)
        print(cookies[1].value)
        print(cookies[1].domain)
        print(cookies[1].path)
        print(cookies[1].expires)
        print(cookies[1].secure)
        print(datetime.datetime.fromtimestamp(cookies[1].expires))
    else:
        print("Không có đủ cookies để truy xuất.")
