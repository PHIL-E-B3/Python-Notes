def howMany(items_list):
    numbers = 0
    strings = 0
    for elem in items_list:
        try:
            x = float(elem)
            numbers = numbers + 1
        except:
            strings = strings + 1
    print("There are", len(items_list), "elements:\n",
          numbers, "are numbers\n", strings, "are strings")
    return [numbers, strings]


# main
z = [2, 'a', 'b', 7, 1, 5, 4, 'z']
res = howMany(z)
print("The values obtained are:", res)
