my_dict={'name':'Jack','age':26}
print(my_dict['name'])
print(my_dict.get('age'))

print("update value")
my_dict['age']=27
print(my_dict)

print("add item")
my_dict['address']='Downtown'
print(my_dict)

squares={1:1,2:4,3:9,4:16,5:25}
print(squares)

print('remove a particular item')
print(squares.pop(4))
print(squares)

print('remove an arbitary item')
print(squares.popitem())
print(squares)

print('remove all items')
squares.clear()
print(squares)

print('delete the dictionary itself')
del squares

squares={1:1,3:9,5:25,7:49,9:81}
print(1 in squares)
print(2 not in squares)

print('membership tests for key only not value')
print(49 in squares)