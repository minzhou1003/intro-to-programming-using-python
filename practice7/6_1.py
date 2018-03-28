# minzhou@bu.edu


def getPentagonalNumber(n):

    return int((n*(3*n - 1)) / 2)


def main():

    print('The first 100 pentagonal number are:')

    for i in range(1, 101):
        print(str(getPentagonalNumber(i)) + ' ', end='')
        if i % 10 == 0:
            print('\n')

main()