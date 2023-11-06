text = input('Enter a string: ')

if len(text) < 4:
    result = ""
else:
    result = text[:2] + text[-2:]

print("The result is:")
print(result)
