def ratio(num, den):
    ''' Calculate the ratio between the numbers provided
    as inputs and write the result on the screen
    INPUT: num = numerator; den = denominator '''
    
    try:
        print("The ratio between", num, "and", den,
              "is:", num/den)

    except ZeroDivisionError:
        print("ERROR: null denominator")

    except TypeError:
        print("ERROR: non-numeric input")

