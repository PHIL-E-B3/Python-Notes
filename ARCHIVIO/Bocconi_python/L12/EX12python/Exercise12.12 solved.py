# FUNCTION
def price(p, v=22):
    ''' Calculate the price of a product by applying
    the specified VAT rate and write its value on the screen 
    INPUT: p = price (VAT excluded); v = Tax rate '''
    
    v = v/100
    print("Price (VAT excluded): ", format(p, '.2f'))
    print("Price (VAT included): ", format(p*(1+v), '.2f'))


# MAIN program
product_price = float(input("Price: "))

try:
    product_vat = float(input("VAT rate (in %) \
['n' to skip this input]: "))

    # Function execution (specifying the optional argument)
    price(product_price, product_vat)

except ValueError:
    # Function execution (using the default value)
    price(product_price) 
