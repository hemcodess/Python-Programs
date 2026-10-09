tpl = ('item1', 'item2', 'item3', 'item4', 'item5')
len(tpl)
print(tpl)
print(tpl[0])
print(tpl[1])
print(tpl[2])
print(tpl[3])
print(tpl[4])
print(tpl[-1])
print(tpl[-2])
print(tpl[-3])
print(tpl[-4])
print(tpl[-5])
last_index = len(tpl) - 1
print(tpl[last_index])

#slicing
print(tpl[0:2])
print(tpl[1:3])
print(tpl[2:4])
print(tpl[3:5])
print(tpl[:3])
print(tpl[2:])
print(tpl[:])

print(tpl[-1:-3])
print(tpl[-3:-1])
print(tpl[-2:])
print(tpl[:-2])

#changing tuple to lists
tpl = ('item1', 'item2', 'item3', 'item4', 'item5')
lst = list(tpl)
print(lst)
lst[0] = 'item0'
print(lst)

#converting list to tuple
lst = ['item1', 'item2', 'item3', 'item4', 'item5']
tpl = tuple(lst)
print(tpl)

#checking an item in tuple
tpl = ('item1', 'item2', 'item3', 'item4', 'item5')
print('item3' in tpl)
print('item6' in tpl)

#checking an item not in tuple
tpl = ('item1', 'item2', 'item3', 'item4', 'item5')
print('item3' not in tpl)
print('item6' not in tpl)

#joining tuple
tpl1 = ('item1', 'item2', 'item3', 'item4', 'item5')
tpl2 = ('item6', 'item7', 'item8', 'item9', 'item10')
tpl3 = tpl1 + tpl2
print(tpl3)

#delete tuple
del tpl