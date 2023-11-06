# FUNCTION

def TelefMob():
    '''Function to generate mobile phone numbers'''
    
    import random

    number = random.randint(300000001, 999999999)
    # number = random.randrange(300000001, 1000000000)  # alternatively

    phone = '3' + str(number)

    return phone



# MAIN program

print("Code", "Phone Number", sep = '\t')

for x in range(1,6):
    print("CL10"+str(x), TelefMob(), sep = '\t')
