# FUNCTION
def digits_sum(number):
    x = str(number)
    mySum = 0
    for i in x:
        mySum = mySum + int(i)
    return mySum

# MAIN Program
x = 17 
print("The digits sum of", x, "is", digits_sum(x))
x = 153
print("The digits sum of", x, "is", digits_sum(x))
