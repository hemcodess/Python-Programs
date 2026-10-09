empty_dist = {}
dct = {'a': 1, 'b': 2, 'c': 3}

print(empty_dist)
print(dct)

print(dct['a'])
print(dct['b'])
print(dct['c'])

print(len(dct))
print(dct.get('a'))
print(dct.get('b'))
print(dct.get('c'))

print('a' in dct)
print('b' in dct)
print('c' in dct)

print('a' not in dct)
print('b' not in dct)
print('c' not in dct)

dct['d'] = 4
print(dct)

dct['d'] = 5
print(dct)

dct.update({'e': 6, 'f': 7})
print(dct)
dct['a'] = 10
print(dct)

dct.pop('a')
print(dct)

dct.popitem()
print(dct)

dct.clear()
print(dct)

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
print(dct.keys()) # dict_keys(['key1', 'key2', 'key3', 'key4'])
print(dct.values()) # dict_values(['value1', 'value2', 'value3', 'value4'])

dct_copy = dct.copy()
print(dct_copy)

#getting dictionary keys as a list
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = list(dct.keys())
print(keys)

#getting dictionary values as a list
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = list(dct.values())
print(values)