# FUNCTION
def digits_sum_bis():
    x = input("Enter a positive integer number: ")
    try:
        if x == '':
            print("You pressed Enter without typing anything")
        elif float(x) != int(float(x)): # to check if a number is not an integer
            print("You entered a number with decimals")
        elif int(x) < 0 :
            print("You entered a negative number")
        elif int(x) == 0:
            print("You entered a null value")
        else:
            mySum = 0
            for i in x:
                mySum = mySum + int(i)
            print("The digits sum of", x, "is", mySum)
    except:
        print("You entered a text string instead of a number")

# MAIN program
digits_sum_bis()
