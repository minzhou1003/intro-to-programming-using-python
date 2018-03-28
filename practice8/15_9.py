# minzhou@bu.edu


def reverseDisplay(value):

    if len(value) == 0:
        return
    print(value[-1], end='')
    reverseDisplay(value[:-1])


def main():
    value = input('Enter a string: ')
    reverseDisplay(value)


if __name__ == '__main__':
    main()
    