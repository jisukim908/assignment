import requests

data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', data=data)
print(response.text)
print(response.status_code)