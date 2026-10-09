lst = list() #using built in function
empty_list = list()
print(len(empty_list))

lst=[]
empty_list = []
print(len(empty_list))

fruits = ['apple', 'banana', 'orange', 'mango']
print('Fruits:', fruits)
print(len(fruits))

lst = ['hema', 22, True, 3.24, {'age': 22, 'country': 'India'}] #list of different items

#accesing elements
lst_t = fruits[0]
print(lst_t)

print(fruits[1])
print(fruits[2])
print(fruits[3])
#print(fruits[4]) #IndexError: list index out of range
print(len(fruits)-1)
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])
#print(fruits[-5]) #IndexError: list index out of range


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first, second, third, *rest, tenth = numbers
print(first) #1
print(second) #2
print(third) #3
print(rest) #[4, 5, 6, 7, 8, 9]
print(tenth) #109


#slicing items in list
fruits = ['apple', 'banana', 'orange', 'mango', 'grapes']
all_fruits = fruits[0:4]
print(all_fruits)
all_fruits = fruits[0:]
print(all_fruits)
all_fruits = fruits[:4]
print(all_fruits)

#updating list
fruits[0] = 'kiwi'
print(fruits)

#deleting items in list
del fruits[4]
print(fruits)
fruits = ['apple', 'banana', 'orange', 'mango']
del fruits[1:3]
print(fruits) 
#checking items in list
does_exist = 'apple' in fruits
print(does_exist)  #False
does_exist = 'kiwi' in fruits
print(does_exist) #True

#adding items in list
lst = list()
lst.append('hema')
print(lst)
lst.append('akhil')
print(lst)

#inserting items in list
lst = ['item1', 'item2', 'item3'] 
lst.insert(0, 'item0')
print(lst)
lst.insert(4, 'item4')
print(lst)

#removing items in list
lst = ['item1', 'item2', 'item3', 'item4', 'item5']
lst.remove('item3')
print(lst)

#removing last item in list
lst.pop()
print(lst)
lst.pop(1)
print(lst)

lst = ['item1', 'item2', 'item3', 'item4', 'item5']
del lst[0]
print(lst)
del lst[1]
print(lst)
del lst[1:2]
print(lst)
#del fruits
#print(fruits) # NameError: name 'fruits' is not defined

#clearing list
lst = ['item1', 'item2', 'item3', 'item4', 'item5']
lst.clear()
print(lst)

#copying list
lst = ['item1', 'item2', 'item3', 'item4', 'item5']
lst2 = lst.copy()
print(lst2)

#joining list
lst = ['item1', 'item2', 'item3', 'item4', 'item5']
lst2 = ['item6', 'item7', 'item8', 'item9', 'item10']
lst3 = lst + lst2
print(lst3)

#repeating list
lst = ['item1', 'item2', 'item3', 'item4', 'item5']
lst2 = lst * 3
print(lst2)

#counting items in list
lst = ['item1', 'item2', 'item3', 'item4', 'item5']
print(lst.count('item1'))
print(lst.count('item2'))
print(lst.count('item3'))
print(lst.count('item4'))
print(lst.count('item5'))
print(lst.count('item6'))

#sorting list
lst = ['mango', 'apple', 'banana', 'orange', 'kiwi']
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)

#reversing list
lst = ['mango', 'apple', 'banana', 'orange', 'kiwi']
lst.reverse()
print(lst)

#nested list
lst = [['item1', 'item2', 'item3'], ['item4', 'item5', 'item6'], ['item7', 'item8', 'item9']]
print(lst)
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[0][0])
print(lst[0][1])
print(lst[0][2])
print(lst[1][0])
print(lst[1][1])
print(lst[1][2])
print(lst[2][0])
print(lst[2][1])
print(lst[2][2])

#list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)

