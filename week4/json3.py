import json

# Python 객체
data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Python 객체를 JSON 파일로 변환
with open('data2.json', 'w') as file:
    json.dump(data, file)