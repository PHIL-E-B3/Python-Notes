
while True:
    num1 = int(input('Enter the first number (0-10): '))
    if num1 >= 0 and num1 <= 10:
        break
    else:
        print('First number must be between 0 and 10 (both included). Try again!')        

while True:
    num2 = int(input('Enter the second number (greater than 10): '))
    if num2 >= 10:
        break
    else:
        print('The second number must be greater than 10. Try again!')
        

for n in range(num1, num2+1):
    if n % 3 == 0 or n % 5 == 0:
        continue
    print(n)






