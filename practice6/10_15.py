# minzhou@bu.edu

def isSorted(lst):

    return sorted(lst) == lst


def main():

    lst = list(map(int, input('Enter list: ').split()))

    if isSorted(lst):
        print('The list is already sorted')

    else:
        print('The list is not sorted')

main()