import requests
with open('file.txt','rb') as file:
    file = {'file':file}
    requests = requests.post('https://www.example.com/upload', file)

data = {
    "id": 1,
    "title": "hello world",
    "body": "tesst",
}

response = requests.get('https://jsonplaceholder.typicode.com/posts', json=data)

print('status code',response.status_code)
print('body', response.text)
print(response.json())