# FUNCTION
def area_tri(base, height):
    ''' Calculate the area of a triangle
    INPUT:
    base = base of the triangle
    height = height of the triangle
    OUTPUT:
    area = area of the triangle '''
    
    area = (base*height)/2
    return area


# MAIN program

b = float(input("Base of the triangle: "))
h = float(input("Height of the triangle: "))

a = area_tri(b, h) # Function execution
print("Area of the triangle:", a)
