from urllib.request import urlopen
from urllib.request import Request
import gzip

req = Request("https://utc.edu.vn/")
#req.add_header("Accept-Language", "en")
req.add_header("Accept-Encoding", "gzip")
response = urlopen(req)
data = gzip.decompress(response.read())
#c = response.read()
print(data)
# r = urlopen("https://www.utc.edu.vn")
# print(r.url)
# print(r.status)
# c = r.read()
# c1 = r.readlines()
#print(c)
#print(c1)