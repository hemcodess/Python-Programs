#if statement
temperature = 30

if temperature > 40:
   print("It's Hot")

print("Check complete")

#if else statement
age = 16

if age >= 18:
   print("Eligible for voting")
else:
   print("Not Eligible")


#if-elif-else block
marks = 75

if marks >= 90:
   print("Excellent")
elif marks >=40:
   print("Pass")
else:
   print("Fail")

#Nested if statements
age = 16
has_id = True

if age >= 18:
    if has_id:
       print("Access allowed")
    else:
       print("Not allowed")
else:
   print("Too young")


print("Done")

#Truthy and falsy values 
name = "Hema"

if name:
   print("Name is available")
else:
   print("name is not available")

name = ""

if name:
   print("Name is available")
else:
   print("Name is empty")

items = []

if  items:
   print("Items found")
else:
   print("List is Empty")

print ("Finished")

#pass statement
marks = 75

if marks >= 45:
   pass
else: 
   print("Fail")

print("Finished")

num = int(input("Enter a number"))
print ("Your number is", num)
if num > 0:
   print("Positive")
elif num < 0:
   print("Negative")
else:
   print("Zero")

#if condition with logical operators
a = 0
if a > 0 and a % 2 == 0:
   print("A is even and positive integer")
elif a > 0 and a % 2 != 0:
   print("A is positive integer")
elif a == 0:
   print("A is zero")
else:
   print("A is negative")