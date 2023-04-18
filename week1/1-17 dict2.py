person = {'name': 'jisu', 'age': 25, "gender": 'female'}
items = person.items()
print(items)
# dict_items([('name', 'jisu'), ('age', 25), ('gender', 'female')])


# person.clear()
# print(person)  # {}

name = person.get('name')
print(name)  # jisu

email = person.get('email')
print(email)  # None

email = person.get('email', 'unknown')
print(email)  # unknown

print('name' in person)  # True
print('email' in person)  # False
