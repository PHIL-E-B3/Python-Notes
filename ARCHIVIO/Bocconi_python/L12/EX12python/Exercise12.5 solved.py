import math

dir(math)

help(math.ceil)
help(pow)
help(math.log)
help(math.sqrt)
help(abs)


VAL = int(input("Insert an integer number (positive or negative): "))

print("Entered value:", VAL, sep = "\t")
print("# Calculations #")

print("- Absolute value:", abs(VAL), sep = "\t")

print("- Square:", VAL**2, sep = "\t\t")

print("- Cube:", pow(VAL, 3), sep = "\t\t\t")

try:
    print("- Square root:", math.sqrt(VAL), sep = "\t\t")
except:
    print("- Square root:", 'Cannot be calculated', sep = "\t\t")

try:
    print("- Natural logarithm:", math.log(VAL), sep = "\t")
    print("- Base 10 logarithm:", math.log10(VAL), sep = "\t")
except:
    print("- Natural logarithm:", 'Cannot be calculated', sep = "\t")
    print("- Base 10 logarithm:", 'Cannot be calculated', sep = "\t")


