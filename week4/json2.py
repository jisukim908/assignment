import json

# JSON 파일읽기 data.json 지워버림..ㅎㅎ
with open('data.json') as file:
    data = json.load(file)

# Python 객체 출력
print(data)
print(type(data))