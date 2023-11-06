import math

amount = float(input("Total purchase in euros (max 9999.99): "))

if amount > 240:
    discPerc = 0.12
elif amount > 120:
    discPerc = 0.08
elif amount > 70:
    discPerc = 0.05
elif amount > 30:
    discPerc = 0.03
elif amount >= 0:
    discPerc = 0
# ATTENTION: if amount<0 the discPerc variable won't be defined,
# thus the following line of code will (correctly) return an error

discPrice = math.floor(amount * (1 - discPerc))

discValue = amount - discPrice

print("\nFull price:\t", format(amount, "8,.2f") + " EUR", sep = '\t')
print("Applied discount:", format(discPerc, ".0%"))
print("Discount value:\t", format(discValue, "8,.2f") + " EUR", sep = '\t')
print("\\--------------------------------------\\")
print("Discounted price:", format(discPrice, "8,.2f") + " EUR", sep = '\t')

