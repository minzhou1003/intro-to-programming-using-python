# copyright minzhou@bu.edu

def cramer(a, b, c, d, e, f):
    if a * d - b * c == 0:
        print('The equation has no solution')
    else:
        x = (e*d - b*f)/(a*d - b*c)
        y = (a*f - e*c)/(a*d - b*c)
        print('x is %.1f and y is %.1f' % (x, y))

[a, b, c, d, e, f] = list(map(float, input('Enter a, b, c, d, e, f: ').split(',')))
cramer(a, b, c, d, e, f)