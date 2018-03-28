# minzhou@bu.edu

from random import randint

def countIntegers():

    # Count the number of occurrence of the random number
    counts = [0]*10

    for i in range(1000):
        num = randint(0, 9)
        counts[num] += 1
    
    return counts

def main():
    res = ' '.join(map(str,countIntegers()))

    print('The counts for random integers form 0 to 9 are: ', res)

main()