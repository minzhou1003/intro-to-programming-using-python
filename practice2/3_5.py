# copyright minzhou@bu.edu

import math

def poly_area(n, s):
    area = ((n * (s**2)) / (4 * (math.tan(math.pi / n))))
    return area

n = int(input('Enter the number of sides: '))
s = float(input('Enter the side: '))
print('The area of the polygon is ' + str(poly_area(n, s)))
