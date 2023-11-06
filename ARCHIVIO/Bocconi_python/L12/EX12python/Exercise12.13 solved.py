
max_val = input("Insert a number: ")
prime_list = ""

try:
    max_val = int(max_val)
    if max_val <= 0:
        print("Invalid number (null or negative)")
    elif max_val == 1:
        print("Prime list: 1")
    elif max_val == 2:
        print("Prime list: 1, 2")
    else:
        for x in range(3, max_val+1, 2):
            prime = True
            for i in range(3, x):
                if x % i == 0: # if a divisor of the x number is found...
                    prime = False # ...the x number cannot be a prime number
                    break
            if prime: # only prime numbers will be concatenated to prime_list
                prime_list = prime_list + ", " + str(x)
        print("Prime list: 1, 2" + prime_list)
except:
    print("Invalid input")
