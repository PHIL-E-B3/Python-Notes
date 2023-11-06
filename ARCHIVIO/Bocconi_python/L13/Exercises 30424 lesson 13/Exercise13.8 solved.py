tuplex = (4, 9, ['a','b'], 123.45, 0)
print("Initial tuple:", tuplex)

# tuples are immutable, so we can't add new elements
# converting the tuple to a list is a good way to modify tuples
listx = list(tuplex)
print(listx)

listx.append(7)
print(listx)

listx.insert(3, (10, 100, 1000)) # 4th position = index 3
print(listx)

listx.insert(2, 'bob') # "bob" is stored in position 2, shifting to the right the other values
print(listx)

listx.insert(0, 3.5)
print(listx)

listx.insert(-1, False) # False is stored in position -1, shifting to the right the other values
print(listx)

listx.remove(9)
print(listx)

listx.pop(-4)
print(listx)

# convert to a tuple
tuplex = tuple(listx)
print("Final tuple:", tuplex)
