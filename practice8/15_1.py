# minzhou@bu.edu


def sumDigits(num):
    if num == 0:
        return 0
    return num % 10 + sumDigits(num // 10)


def main():
    num = int(input('Enter a number: '))
    print (sumDigits(num))


if __name__ == '__main__':
    main()