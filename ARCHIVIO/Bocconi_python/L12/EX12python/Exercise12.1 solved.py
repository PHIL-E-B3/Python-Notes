# FUNCTION
def welcome(name, surname):
    ''' Print a welcome message on the screen
    INPUT: name; surname'''
    
    print("Welcome", name, surname)


# MAIN program

n = input("Enter the name: ")
s = input("Enter the surname: ")

welcome(n, s) # Function execution
