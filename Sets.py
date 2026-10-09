st = set()

st.add(1)
st.add(2)
st.add(3)
st.add(4)
st.add(5)

print(st)

st.remove(4)
print(st)

st.clear()
print(st)

st = {1, 2, 3, 4, 5}
print("Length of set st:", len(st))
print("Does set st contain 3? ", 3 in st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True
print('apple' in fruits ) # False
st.add(6)
print(st)
st.update({7, 8, 9})
print(st)
stt ={10,11}
st.update(stt)
print(st)

st1 = {1, 2, 3, 4}
st2 = {3, 4, 5, 6}
print(st1.union(st2))
print(st1.intersection(st2))
print(st1.difference(st2))
print(st2.difference(st1))

st1 = {1, 2, 3, 4}
st2 = {3, 4, 5, 6}
print(st1|st2)
print(st1&st2)
print(st1-st2)
print(st2-st1)

st.remove(1)
print(st)
st.pop()
print(st)
st.clear()
print(st)

st = {1, 2, 3, 4, 5}
print(st)
st.discard(2)
print(st)
st.discard(5)
print(st)
del st
#print(st) # This will raise an error since st is deleted

#convert list to set
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered
print(st)


st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st3 = st2.issubset(st1) # True
st4 = st1.issuperset(st2) # True
print(st3)
print(st4)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
op = python.issubset(dragon)     # False
print(op)

# finding symmetric difference between two sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st3 = st2.symmetric_difference(st1) # {'item1', 'item4'} : st2 ^ st1
print(st3)

# checking if two sets are disjoint
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st3 = st2.isdisjoint(st1) # False
print(st3)