# minzhou@bu.edu


def computeCommission(salesAmount):

    balance = commission = 0.0
    if salesAmount >= 10000.01:
        balance = salesAmount - 10000
        commission += balance * 0.12

    if salesAmount >= 5000.01:
        balance -= balance - 5000
        commission += balance * 0.10

    if salesAmount >= 0.01:
        commission += balance * 0.08

    return commission


def main():

    print("SalesAmount     Commission\n")
    for i in range(10000, 100001, 5000):
        print('{0:<10}     {1:10}'.format(i, computeCommission(i)))


main()