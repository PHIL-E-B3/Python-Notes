def funTickets(day = 'wrk', vision = '2D'):
    """
    Calculation of the ticket price
    - day: 'wrk'=workdays, 'hol'=public holidays
    - vision: '2D', '3D'
    """

    # ticket price
    basePrice = 7
    filmPrice = basePrice

    if day == 'hol':
        filmPrice = filmPrice + 2

    if vision == '3D':
        filmPrice = filmPrice + 2.5


    # customer data and verifications
    try:
        age = int(input("What's your age? "))
        if age < 0 or age > 120:
            print("The value entered is not acceptable.\nPlease try again.")
            age = int(input("What's your age? "))
    except: 
        print("The value entered is not a number.\nPlease try again.")
        age = int(input("What's your age? "))

    # final price 
    if age <= 11:
        filmPrice = filmPrice - 3
    elif (age >= 12 and age <= 15) or age > 64:
        filmPrice = filmPrice * (1-0.15)

    return filmPrice

# MAIN program
price = funTickets('wrk', '2D')
print('\nYour ticket costs', format(price, '.2f'), "€")
