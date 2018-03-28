# minzhou@bu.edu


def reverseDisplay(value):

    reverseDisplayHelper(value, len(value) - 1)


def reverseDisplayHelper(s, high):

    if high < 0:
        return

    print(s[high], end='')
    reverseDisplay(s[:high])


def main():

    value = input('Enter a string: ')
    reverseDisplay(value)
    # reverseDisplayHelper('Python', 4)

if __name__ == '__main__':
    main()
