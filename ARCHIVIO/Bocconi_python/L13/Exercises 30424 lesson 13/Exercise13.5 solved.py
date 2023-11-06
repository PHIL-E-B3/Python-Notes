number = int(input("Enter a number: "))

# create a list containing numbers from 2 to the given number (excluded)
interval = list(range(2, number))

# empty list to store divisors
divisors_list = []

# loop structure to find the divisors and append them to the list
for n in interval:
    if number % n == 0:
        divisors_list.append(n)

# display the result
if len(divisors_list) == 0:
    print('The given number has no divisors, so it is a prime number')
else:
    print('The list of divisors of the given number (' \
          + str(number) + ') is the following:')
    print(divisors_list)
