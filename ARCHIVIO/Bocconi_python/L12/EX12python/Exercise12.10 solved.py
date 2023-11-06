# FUNCTION
def psw_generator():
    import random
    quest = input('Insert the number of digits of your password\n\
(Press "Enter" for an eight-digits password): ')
    # the conversion to int mustn't be executed here in order to
    # allow the user to insert an empty string (by pressing "Enter")

    if quest == "":
        quest = 8
    
    psw = ''
    try:
        psw_len = int(quest)
        for x in range(psw_len):
            psw = psw + str(random.randint(0,9))

    except:
        print("Invalid length")

    return psw


# MAIN Program
print(psw_generator())
