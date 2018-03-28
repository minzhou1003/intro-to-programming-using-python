# minzhou@bu.edu

def locateLargest(a):
    row = 0
    col = 0
    largest = a[0][0]

    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] > largest:
                row = i
                col = j
                largest = a[i][j]

    return (row, col)


def main():

    a = []
    n = int(input('Enter the number of rows in the list: '))

    for i in range(n):
        tmp = list(map(float, input('Enter a row: ').split()))
        a.append(tmp)

    print('The location of the largest element is at', locateLargest(a))

main()