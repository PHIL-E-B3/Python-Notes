import random

n = int(input("How many rolls do you want to simulate (1 to 4)? "))

if n > 4:
    print("You want me to work too much!")

elif n == 1:
    L = random.randint(1, 8)  # 1 and 8 included
    # alternatively: L = random.randrange(1, 9)
    print("\nResult of the eight-sided die roll:", L)
    print("The average score corresponds to the roll's result")

else:
    tot = 0
    print("\nResults of the eight-sided die rolls:")
    for i in range(1, n+1):
        L = random.randint(1, 8)
        tot = tot + L
        print(L, end = "\t")
    avrgScore = round(tot / n, 1)
    print("\nAverage score:", avrgScore)
