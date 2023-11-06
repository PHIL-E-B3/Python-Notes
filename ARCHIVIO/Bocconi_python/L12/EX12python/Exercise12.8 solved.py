# FUNCTION
def loan_installment(i, n, C):
    ''' Calculate the monthly payment of a fixed rate mortgage and constant installments
    INPUT:
    C = loan amount
    i = interest rate (on monthly base)
    n = number of installments
    OUTPUT:
    R = monthly installment '''
    
    i = i/100
    R = (C*i)/(1-(1/(1+i)**n))  # Installment calculation
    return R


# MAIN

try:
    pv   = float(input("Loan amount: "))
    rate = float(input("Monthly interest rate (expressed in %): "))
    nper = float(input("Number of monthly installments: "))

    # Function execution
    pmt = loan_installment(rate, nper, pv) 

    # Monthly installment display (with 2 decimal places)
    print("Monthly installment:", format(pmt, ".2f")) 

except:
    print("ERROR: one or more inputs have not been entered correctly")


