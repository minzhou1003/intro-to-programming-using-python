# minzhou@bu.edu

import random

def shuffle(lst):

    n = len(lst)

    for i in range(n-1, 0, -1):
        j = random.randint(0, i)
        # Swap
        lst[i], lst[j] = lst[j], lst[i]

    return lst


def main():
    lst = input('Enter a list of numbers seperated by comma: ').split(',')
    shuffled_lst = shuffle(lst)
    print('Shuffled list is', list(map(int, shuffled_lst)))


main()