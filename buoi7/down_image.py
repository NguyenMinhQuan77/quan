import urllib.request

print('starting download')
url = 'https://www.utc.edu.vn/assets/utc/images/logo.png'
urllib.request.urlretrieve(url, 'python.png')
with urllib.request.urlopen(url) as r:
    print('status: ', r.status)
    print('downloading python.png')
    with open('python.png', 'wb') as image:
        image.write(r.read())