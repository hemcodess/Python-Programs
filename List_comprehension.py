#one way
language = 'PYTHON'
lst = list(language)
print(type(lst))
print(lst)
#second way: List comprehension
lst = [i for i in language]
print(type(lst))
print(lst)
#ex 1
even_numbers = [i for i in range(20) if i % 2 == 0]
print(even_numbers)
#ex 2
odd = [i for i in range(20) if i % 2 != 0]
print(odd)
#ex 3
numbers = [-8,-7,-3,-1, 0, 1, 3, 4, 7, 8, 10]
positivenums = [i for i in numbers if i % 2 == 0 and i > 0]
print(positivenums)
#ex 4
lstoflists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [n for row in lstoflists for n in row]
print(flattened_list)

#Lambda Function