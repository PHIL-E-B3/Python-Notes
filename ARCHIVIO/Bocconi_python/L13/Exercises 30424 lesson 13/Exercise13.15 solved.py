# FUNCTION
def total_list(numbers):
    result = 0
    for element in numbers:
        result = result + element
    return result


# MAIN Program
X = [1,2,3,4,5,6,7,8,9,10]
X_tot = total_list(X)
print("The total of", X, "is", X_tot)

X = [0.5, 2.4, -1.3, 4, 8.1]
X_tot = total_list(X)
print("The total of", X, "is", X_tot)
