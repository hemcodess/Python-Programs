print("Hello HEMA")
#This is my first comment.
"""This id multiline comment.
This is second line.
This is third line."""
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(3 / 2)
print(3 ** 2) #Exponential
print(3 // 2) #Floor division operator
print(3 % 2)
print(x := 5) #Assignment operator

# Checking data types

print(type(10))          # Int
print(type(9.8))        # Float
print(type(1 + 3j))      # Complex number
print(type("Hello"))     # String
print(type([1, 2, 3]))   # List(ordered and similar to array)
print(type({'name': 'Hema'})) # Dictionary (unordered key value pair)
print(type({1.1, 2.2, 3.3}))  # Set (unordered collection of unique elements)
print(type((1.1, 2.2, 3.3)))  #Tuple (ordered collection of different data types but immutable)
print(type(True))             # Boolean
print(type(lambda x: x + 1))  # Function
print(type(None))             # None