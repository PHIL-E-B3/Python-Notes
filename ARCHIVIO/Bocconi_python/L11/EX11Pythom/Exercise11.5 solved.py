# assignment of the value to VAR variable
# NB: test the program using different types of data
VAR = "x"

# test
if (type(VAR) == int):
    print("The variable is an Integer")
elif (type(VAR) == float):
    print("The variable is a Float")
elif (type(VAR) == bool):
    print("The variable is a Bool")
elif (type(VAR) == str):
    print("The variable is a String")
# residual case (none of the previous condition is true)
else:   
    print("The variable doesn't belong to any of the provided types")

