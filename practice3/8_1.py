# copyright minzhou@bu.edu


def validSSN():
    s = input('Enter a Social Security number: ')
    if len(s) == 11:
        a = s.split('-')
        if len(a[0]) == 3 and len(a[1]) == 2 or len(a[-1]) == 4:
            for i in a:
                if i.isdigit():
                    print('Valid SSN')
                    return True
    else:
        print('Invalid SSN')

validSSN()
