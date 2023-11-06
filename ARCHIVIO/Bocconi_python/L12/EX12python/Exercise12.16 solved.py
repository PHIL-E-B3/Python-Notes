# FUNCTION
def OK_calc(pNetAmount, pWorkType = "Standard"):
    """
    WorkType can only be:
    - Standard
    - Reduced
    - Maintenance
    """
    if pWorkType == "Standard":
        VATrate = 0.22
    elif pWorkType == "Reduced":
        VATrate = 0.04
    elif pWorkType == "Maintenance":
        VATrate = 0.1
    else:
        VATrate = -1

    if VATrate == -1:
        calc = "Error: wrong type of work"
    else:
        calc = pNetAmount * (1 + VATrate)

    return calc


# MAIN program
WorkType = input("Insert the Type of Work (Standard/Reduced/Maintenance): ")
NetAmount = float(input("Insert the Net Amount: "))
GrossAm = OK_calc(NetAmount, WorkType)
if GrossAm == "Error: wrong type of work":
    print(GrossAm)
else:
    print("Type of Work:", WorkType)
    print("Net taxable:", format(NetAmount, ',.2f'), "EUR")
    print("Gross taxable:", format(GrossAm, ',.2f'), "EUR")


