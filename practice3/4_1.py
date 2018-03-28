# copyright minzhou@bu.edu

import math
def quadratic(a, b, c):
    discriminant = pow(b,2) - 4 * a * c
    if discriminant < 0:
        print('The equation has no real roots')
    elif discriminant == 0:
        r1 = (-b + math.sqrt(discriminant)) / (2 * a)
        print('The root is ' + str(r1))
    else:
        r1 = (-b + math.sqrt(discriminant)) / (2 * a)
        r2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print('The roots are ' + str(r1) + ' and ' + str(r2))

[a, b, c] = list(map(float, input('Enter a, b, c: ').split(',')))

quadratic(a, b, c)
