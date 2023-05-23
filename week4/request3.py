import requests

data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', data=data)
print(response.text)
print(response.status_code)

response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(response.text)
print(response.status_code)