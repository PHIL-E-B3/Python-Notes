# FUNCTION
def Distance3D(x1, y1, z1, x2 = 0, y2 = 0, z2 = 0, metrics = 'p'):
    '''Function to calculate the distance between two points P1 and P2
in three-dimensional space. Types of metrics available:
'p' = Pythagorean; 'm' = Manhattan; 'c' = Chebyshev
If the coordinates of the second point are omitted, the function
calculates the distance of the given point from the origin.'''
    import math
    
    if metrics == 'p':
        return math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
    elif metrics == 'm':
        return abs(x1-x2)+abs(y1-y2)+abs(z1-z2)
    elif metrics == 'c':
        return max(abs(x1-x2), abs(y1-y2), abs(z1-z2))
    else:
        print("Invalid 'metrics' argument")
