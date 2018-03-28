# minzhou@bu.edu

def distinct_number():
    numbers = list(input('Enter ten numbers: ').split())
    distinct = []
    for num in numbers:
        if num in distinct:
            continue
        else:
            distinct.append(num)
    print('The distinct numbers are ' + ' '.join(distinct))

distinct_number()