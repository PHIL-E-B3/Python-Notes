# FUNCTION
def stocks(val1, val2):
    '''Calculates the variation in a share price with respect to the initial value
    INPUT: val1 = initial price; val2 = final price
    OUTPUT: stock_var = price variation (in decimal format) '''

    stock_var = (val2-val1)/val1 # Calculate the variation (in decimal format)
    return stock_var


# MAIN program

v1 = float(input("Enter the initial price: "))
v2 = float(input("Enter the final price: "))

var = stocks(v1, v2) # Function execution

# Variation display (% format with 1 decimal digit)
print("Variation:", format(var, ".1%")) 
