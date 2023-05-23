import requests
import json

data = {'title': 'homework', 'body': 'jisukim', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', data=data)
print(response.text)

# result
"""
{
  "title": "homework",
  "body": "jisukim",
  "userId": "1",
  "id": 101
}
"""

# sol1)
result = {
    "title": "homework",
    "body": "jisukim",
    "userId": "1",
    "id": 101
    }

title = result['title']
username = result['body']
user_id = result['userId']
post_id = result['id']

print('Title:', title)
print('User:',username)
print('User ID:', user_id)
print('Post ID:', post_id)


# sol2)
result2 = json.loads(response.text)

file = open("result2.txt", "w")

file.write('title:' + data['title'] + '\n')
file.write('User:'+ data['body'] + '\n')
file.write('User ID:'+ str(data['userId']))

file.close()