

num = abs(int(input('Enter an integer number: ')))


if num == 0:
    print('Invalid number')

else:
    divisors = 0
    for n in range(1, num+1):
        if num % n == 0:
            divisors = divisors + 1
            print(n)
    print('We found', divisors, 'divisors')

