# Variables in Python
first_name = 'A'
last_name = 'Hemalata'
country = 'India'
city = 'Malkangiri'
age = 22
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'A',
   'lastname':'Hemalata',
   'country':'india',
   'city':'Berhampur'
   }

print('My name is', first_name, last_name)
print('Firstname length is', len(first_name))
print('Lastname length is', len(last_name))
print('Country is', country)
print('City is', city)
print('Age is', age)
print('Skills are', skills)
print('Person info is', person_info)

print('My name is', first_name, last_name, 'and I am', age, 'years old')

first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)