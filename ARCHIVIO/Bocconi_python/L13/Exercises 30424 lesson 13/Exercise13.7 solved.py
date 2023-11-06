number = int(input("Enter a number: "))

multiples_list = {}

for n in range(1, 1000):
    if number * n <= 1000:
        multiples_list[n] = number * n
    else:
        break

if len(multiples_list) == 0:
    print('The number has no multiples smaller than 1000')
else:
    print('Multiplication table of', number)
    for key, value in multiples_list.items():
        print(number, "x", format(key, "3d"),
              "=", format(value, "4d"))
