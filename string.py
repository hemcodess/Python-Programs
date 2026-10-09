letter = 'p'
print(letter)
print(len(letter))

multiline_string = '''I am A. Hemalata. I'm studying in MCA. 
I live in Malkangiri. This is my 30 day Python Challenge.'''
print(multiline_string)

first_name = 'A'
space = ' '
last_name = 'Hemalata'
full_name = first_name + space + last_name 
print(full_name)
print(len(first_name))
print(len(last_name))
print(len(full_name))

print('I hope everyone is enjoying the Python Challenge. \nAre you?') #\n Line break
print('Days\tTopics\tExercises') #adding tab space
print('Day 1\t5\t5')
print('Day 2\t5\t5')
print('Day 3\t5\t5')
print('Day 4\t5\t5')
print('Day 5\t5\t5')
print('This is a backslash symbol(\\)')
print('In every programming language it starts with \"Hello, World!\"') #to write a double quote inside a single quote

first_name = 'A'
last_name = 'Hemalata'
language = 'Python'
formated_string = 'I am %s %s. I am learning %s.' %(first_name, last_name, language)
print(formated_string)

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle of radius %d is %.2f.' %(radius, area)
print(formated_string)

python_libraries = ['Django', 'Flask', 'Numpy', 'Pandas', 'Tensorflow', 'PyTorch', 'Matplotlib', 'Seaborn']
formated_string = 'The following are python libraries : %s' %(python_libraries)
print(formated_string)

first_name = 'A'
last_name = 'Hemalata'
language = 'Python'
formated_string = 'I am {} {}. I am learning {}.' .format(first_name, last_name, language)
print(formated_string)
a = 10
b = 20
print('{} + {} = {}'. format(a, b, a + b))
print('{1} + {0} = {2}' .format(a, b, a + b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} ** {} = {}'.format(a, b, a ** b))
print(f'{a} + {b} = {a + b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}') 
print(f'{a} - {b} = {a - b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} ** {b} = {a ** b}')


language = 'Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)
second_last_index = len(language) - 2
second_last_letter = language[second_last_index]
print(second_last_letter)
last_letter = language[-1]
print(last_letter)
second_last_letter = language[-2]
print(second_last_letter)

#slicing

language = 'Python'
first_three_letters = language[0:3]
print(first_three_letters)
last_three_letters = language[-3:]
print(last_three_letters)
one_to_three_letters = language[1:4]
print(one_to_three_letters)
first_three_letters = language[:3]
print(first_three_letters)
last_three_letters = language[3:]
print(last_three_letters)

greeting = 'Hello, World!'
print(greeting[::-1]) #reversing the string

greeting = 'Hello, World!'
print(greeting[::2])

greeting = 'Hello, World!'
pit = greeting[0:6:2]
print(pit) #skipping every other character

challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'
print(challenge.title()) # 'Thirty Days Of Python'
print(challenge.upper()) # 'THIRTY DAYS OF PYTHON'
print(challenge.lower()) # 'thirty days of python'
print(challenge.swapcase()) # 'THIRTY DAYS OF PYTHON'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
print(challenge.split('y')) # ['thir', ' days of python']
print('-'.join(challenge)) # 't-h-i-r-t-y- -d-a-y-s- -o-f- -p-y-t-h-o-n'

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17


first_name = 'A'
last_name = 'Hemalata'
age = 21
job = 'student'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, job, age, country)
print(sentence) # I am A Hemalata. I am a student. I am 21 years old. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 7
 #print(challenge.rindex(sub_string, 9)) # error
print(challenge.rindex('on', 8)) # 19

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
#print(challenge.index(sub_string, 9)) # error

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded

challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed

num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

challenge = 'thirty days of python'
print(challenge.islower()) # True

challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

