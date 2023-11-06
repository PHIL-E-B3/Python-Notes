# FUNCTION
def report(q1, q2, q3, p1=60, p2=57, p3=59):
    ''' Create a report containing the quantities sold in each store
    and the related revenues
    INPUT:
    q1 and p1 = quantity sold and unit price in the Milan store
    q2 and p2 = quantity sold and unit price in the Turin store
    q3 and p3 = quantity sold and unit price in the Rome store'''
    # calculation of store revenues
    r1 = q1*p1 
    r2 = q2*p2
    r3 = q3*p3
    average_q = (q1+q2+q3)/3 # average quantity
    average_r = (r1+r2+r3)/3 # average revenue
    print("Store\t\tQuantity\tRevenue [€]")
    print("Milan", q1, format(r1, ".2f"), sep="\t\t")
    print("Turin", q2, format(r2, ".2f"), sep="\t\t")
    print("Rome", q3, format(r3, ".2f"), sep="\t\t")
    print("MEAN", format(average_q, ".1f"), format(average_r, ".2f"), sep="\t\t")


# MAIN program
try:
    quantity1 = int(input("Quantity sold in the Milan store: "))
    quantity2 = int(input("Quantity sold in the Turin store: "))
    quantity3 = int(input("Quantity sold in the Rome store:  "))
    report(quantity1, quantity2, quantity3)
except ValueError:
    print("ERROR: invalid input")

