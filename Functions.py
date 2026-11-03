def function():
    first_name = "Hema"
    last_name = "lata"
    full_name = first_name + last_name
    print(full_name)
#calling a function
function()

def add():
    first_num = 2
    second_num = 3
    total = first_num + second_num
    return total
print(add())

print("-->Function with parameter")
def greeting(name):
    message = name + ', WELCOME!'
    print(message)
greeting('Hema')

def add(num):
    ten = 10
    return num + ten
print(add(6))

def square(x):
    return x * x
print(square(69))

def area_of_circle(r):
    pi = 3.14
    area = pi * r ** 2
    return area
print(area_of_circle(12))

def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total+=i
    return total
print(sum_of_numbers(10))
print(sum_of_numbers(100))

def sum_of_two_numbers(first_num, second_num):
    sum = first_num + second_num
    return sum
print(sum_of_two_numbers(45, 55))

print("-->Passing arguements with two parameters")
def add(num1, num2):
    total = num1 + num2
    return total
print(add(num1 = 3, num2 = 4)) #order does not matter

print("-->Function returning a value")
def print_full_name(first_name, last_name):
    full_name = first_name + last_name
    return full_name
print(print_full_name(first_name = 'hema', last_name = 'lata'))

def age(currentyear, birthyear):
    current_age = currentyear - birthyear
    return current_age
print(age(2026, 2004))

def even(n):
    if n % 2 == 0:
        return True
    return False
print(even(19))
print(even(8))

#returninng list[]
def even(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(even(10))

print("--> Function with default parameter")
def  greetings(first_name = 'Hema', last_name = 'lata'):
    fullname = first_name + last_name
    return fullname
print(greetings())
print(greetings('sai', 'ram'))

print("")
print("-->Arbitary number of arguements")
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print('sum of all numbers:', sum_all_nums(2, 3, 4, 5, 6))
print("")
print("--> Default and arbitary number of parameters")
def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team-1', 'hema' , 'sai')
print("")
print("Dictionary unpacking")
def greet(name, location):
    print("Hi,", name, " Are you from", location)
greet(name= 'Hema', location = 'Odisha')#without this line, ** operator unpacks the dictionary in below line , passing its key-pairs as keyword arguements to the function
my_dict = {"name": "Hema", "location": "Odisha"}
greet(**my_dict)
print("")
print("-->Arbitary number of named arguements")
def arbitary(**args):
    args = {"name": "Hema", "location": "Odisha"}
    print("i received an arbitary no of args", len(args))
    print("They are provided as a dictionary in my function", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print("*key:",k, "value:", v)
print(arbitary())
print("")
print("-->Function as a parameter of another function")
def square(n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square, 3))