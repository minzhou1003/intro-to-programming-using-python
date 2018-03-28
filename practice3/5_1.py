# copyright minzhou@bu.edu

def ave():
    count_pos = 0
    count_neg = 0
    total = 0
    a = int(input('Enter an integer, the input ends if it is 0: '))
    if a != 0:
        while(True):
            if a == 0:
                break
            if a < 0:
                count_neg += 1
            if a > 0:
                count_pos += 1
            total += a
            a = int(input('Enter an integer, the input ends if it is 0: '))
        print('The number of positives is ', count_pos)
        print('The number of negatives is ', count_neg)
        print('The total is ', total)
        print('The average is ' , float(total/(count_neg + count_pos)))
    else:
            print('''You didn't enter any number''')

ave()
        

        