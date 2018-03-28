# minzhou@bu.edu


def displaySortedNumbers(num1, num2, num3):

    return sorted([num1, num2, num3])

def main():

    nums = list(map(float, input('Enter three numbers: ').split(',')))
    print('The sorted numbers are ' + ' '.join(map(str, displaySortedNumbers(nums[0], nums[1], nums[2]))))

main()