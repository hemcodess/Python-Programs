#while loop
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)


print("example 2")
#break and continue
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1


print("for loop")
numbers = [0,1,2,3,4,5]
for num in numbers:
    print(num)

language = 'PYTHON'
for letter in language:
    print((letter))

for i in range(len(language)):
    print(language[i])

#for loop on tuple
numbers = (0, 1, 2, 3, 4, 5)
for num in numbers:
    print(num)

#for loop with dictionary
person = {
    'name':'Hema',
    'age':22,
    'country':'India'
}
for key in person:
    print(key)
for value in person.items():
    print(value)
for key, value in person.items():
    print(key, value)

#for loop in set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

numbers = (0, 1, 2, 3, 4)
for num in numbers:
    print(num)
    if num == 3:
        break

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue