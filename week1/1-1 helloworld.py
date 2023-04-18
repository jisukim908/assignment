text = "hello world!"
count = text.count("l")
print(count)  # 3

position = text.find("world")
print(position)  # 6

try:
    position = text.index("world")
    print(position)  # 6
except ValueError:
    print('찾는 문자열이 없습니다.')

uppercase_text = text.upper()
print(uppercase_text)  # HELLO WORLD!

lowercase_text = text.lower()
print(lowercase_text)  # hello world!

replaced_text = text.replace("world", "python")
print(replaced_text)  # hello python!
