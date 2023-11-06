import random

num = random.randint(0, 1000)
print("The number generated randomly is:", num)

if num%7 == 0:
    print(num, "is multiple of 7")
else:
    print(num, "is not multiple of 7")
