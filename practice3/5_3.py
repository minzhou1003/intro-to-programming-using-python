# copyright minzhou@bu.edu


def table():
    print('{:s}    {:s}'.format('Kilograms', 'Pounds'))
    for n in range(1, 200):
        print('{:<9d}{:>10.1f}'.format(n, n * 2.2))

table()