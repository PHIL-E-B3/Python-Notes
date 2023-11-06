number = int(input("Enter a number: "))

multiples_list = []

for n in range(1, 1000):
    if number * n <= 1000:
        multiples_list.append(number * n)
    else:
        break

if len(multiples_list) == 0:
    print('The given number has no multiples smaller than 1000')
else:
    print('The list of multiples of the given number (' \
              + str(number) + ') is the following:')
    print(multiples_list)
