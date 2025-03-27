dict1 = {'Key1': 12, 'key2': 122, 'key3': 76, 'key4': '53', 'key5':765}
dict2 = {'a': 14, 'b': 190, 'c': 54}
'''
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(len(dict1))
'''
dict1=dict1 | dict2  # to add 1 dict to another dict
print(dict1)
#A Python dictionary is a data structure that stores the value in key: value pairs. 
# Values in a dictionary can be of any data type and can be duplicated,
# whereas keys can’t be repeated and must be immutable
dict1.get('key4')


