# minzhou@bu.edu


class Location:

    def __init__(self, row, column, maxValue,):
        self.row = row
        self.column = column
        self.maxValue = maxValue


def locateLargest(a):
    maxValue = a[0][0]
    row = 0
    col = 0

    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] > maxValue:
                maxValue = a[i][j]
                row = i
                col = j
    return Location(row, col, maxValue)


def main():
    [row, col] = list(map(int, input('Enter the number of rows and columns in the list: ').split(',')))
    a = []
    for i in range(row):
        temp_row = list(map(float, input('Enter row {}: '.format(i)).split()))
        if len(temp_row) > col:
            raise RuntimeError('Out of Bound Exception: col %d' % col)
        a.append(temp_row)
    locate = locateLargest(a)
    print('The location of the largest element is {} at ({}, {})'.format(locate.maxValue, locate.row, locate.column))


if __name__ == '__main__':
    main()