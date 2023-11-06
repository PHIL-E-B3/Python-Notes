# FUNCTION
def interest(investment, rate, years = 1):
    '''Calculate the interest accrued from an invested capital 
    INPUT:
    investment = invested capital
    rate = annual interest rate
    years = duration of the investment (in years)
    OUTPUT:
    interests = accrued interest '''

    interests = investment*(rate/100)*years
    return interests


# MAIN

c = 1000 # invested capital
r = 2    # interest rate (expressed as a %)
y = 5    # number of years

# Function execution
print("Accrued interest: €",  interest(c, r, y))

