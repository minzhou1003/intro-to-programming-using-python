# copyright minzhou@bu.edu

import math


def area(length):
    s = 2 * length * math.sin(math.pi / 5)
    area = 3 * math.sqrt(3) * (s ** 2) / 2
    return area

length = float(input('Enter the length from the center to a vertex: '))
print('The area of the pentagon is %.2f' % area(length))