#named function
def add(a, b):
    return a + b
print(add(2, 3))

#using lambda function, we need not to use named function
add = lambda a, b: a + b
print(add(2, 3))

#self invoking lambda function
print((lambda a, b: a + b)(2, 3))

#ex
square = lambda x: x ** 2
print(square(3))

cube = lambda x: x ** 3
print(cube(3))

#ex
multiple = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple(5, 5, 3))

#ex
def power(x):
    return lambda n : x ** n
cube = power(2)(3)
print(cube)
print(power(2)(5))