# minzhou@bu.edu


def gcd(m, n):
    if m % n == 0:
        return n
    return gcd(n, m % n)


def main():
    m, n = input('Enter two numbers separated by coma: ').split(',')
    print('The GCD is:', gcd(int(m), int(n)))


if __name__ == '__main__':
    main()