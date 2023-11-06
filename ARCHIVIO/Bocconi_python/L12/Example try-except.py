try:
    a = int(input('Enter a number: '))
    b = int(input('Enter another number: '))
    print(a/b)

except ValueError:
    print('\nEnter integer numbers only!')
except ZeroDivisionError:
    print("\nOne of the two values is 0! \nPlease try again from the beginning with another number")
except:
    print('\nSomething’s wrong: try again with other numbers!')
