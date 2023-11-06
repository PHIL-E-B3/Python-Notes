import random

# random.random generates numbers in [0 - 1), so 1 is not included
x1 = random.random()
x2 = random.random()
x3 = random.random()

for i in (x1, x2, x3):
    print(i)

# sort the numbers (6 possible combinations) and display them
if   x1 >= x2 and x1 >= x3:
    print("1st value: ", format(x1, ".4f"))
    if x2 >= x3:
        print("2nd value: ", format(x2, ".4f"))
        print("3rd value: ", format(x3, ".4f"))
    else:
        print("2nd value: ", format(x3, ".4f"))
        print("3rd value: ", format(x2, ".4f"))
elif x2 >= x1 and x2 >= x3:
    print("1st value: ", format(x2, ".4f"))
    if x1 >= x3:
        print("2nd value: ", format(x1, ".4f"))
        print("3rd value: ", format(x3, ".4f"))
    else:
        print("2nd value: ", format(x3, ".4f"))
        print("3rd value: ", format(x1, ".4f"))
elif x3 >= x1 and x3 >= x2:
    print("1st value: ", format(x3, ".4f"))
    if x1 >= x2:
        print("2nd value: ", format(x1, ".4f"))
        print("3rd value: ", format(x2, ".4f"))
    else:
        print("2nd value: ", format(x2, ".4f"))
        print("3rd value: ", format(x1, ".4f"))

