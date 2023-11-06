# FUNCTION 1
def create_list():
    new_list = []
    n = int(input('Enter the number of elements of your list: '))
    for number in range(n):
        x = int(input('Enter an integer: '))
        new_list.append(x)
    return new_list

# FUNCTION 2
def draw_hist(symbol = '*'):
    myList = create_list()
    for number in myList:
        print(symbol * number)


# MAIN Program
draw_hist('#')
