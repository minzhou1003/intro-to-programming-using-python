# minzhou@bu.edu

import math

# Compute the standard deviation of values
def deviation(x):

    n = len(x)
    tmp = [0]*n
    res = 0

    for i in range(n):
        tmp[i] = (x[i] - mean(x))**2
    res = math.sqrt(sum(tmp) / (n-1))
    return res

# Compute the mean of a list of values
def mean(x):

    return sum(x)/len(x)


def main():
    x = list(map(float, input('Enter numbers: ').split()))
    print('The mean is ', mean(x))
    print('The standard deviation is ', deviation(x))

main()