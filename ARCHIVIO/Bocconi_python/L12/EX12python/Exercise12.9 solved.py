# FUNCTION
def val_average():
    val = 0
    val_sum = 0
    val_num = 0
    while val != "":
        val = input("Insert an exam grade: ")
        if val != "":
            try:
                val = int(val)
                if val < 18 or val > 31:
                    print("Error: value must be between 18 and 31")
                else:
                    val_sum = val_sum + val
                    val_num = val_num + 1
            except:
                print("Invalid value")
    return val_sum / val_num


# MAIN program
print(format(val_average(), ".2f"))
