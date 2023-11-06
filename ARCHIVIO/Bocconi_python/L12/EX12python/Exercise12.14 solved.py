# FUNCTION
def balance_change(old_balance, change):
    ''' Increase/decrease the bank account balance by a specified amount
    INPUT:
    old_balance = initial balance
    change = amount paid (+) or withdrawn (-)
    OUTPUT:
    new_balance = final balance '''
    
    new_balance = old_balance + change
    print("Previous balance: €", old_balance,
          "|| Current balance: €", new_balance)
    return new_balance


# MAIN program
balance = float(input("Enter the initial balance: "))

while True:
    amount = float(input("\nEnter the amount withdrawn (negative) or paid (positive)\n\
Write 0 to finish: "))
    if amount == 0:
        break
    balance = balance_change(balance, amount)

print("\nThe final balance of your bank account is: €", balance)
if balance < 0:
    print("Attention, your account is in the red!")
