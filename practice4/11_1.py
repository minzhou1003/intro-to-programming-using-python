# minzhou@bu.edu


def sumColumn(m, columnIndex):

    res = 0
    for row in range(len(m)):
        res += m[row][columnIndex]
    return res

def main():

    mat = []
    for i in range(3):
        mat.append(list(map(float, input('Enter a 3-by-4 matrix row for row ' + str(i) + ': ').split())))
    for j  in range(4):
        print('Sum of the elements for column '+ str(j) + ' is ', sumColumn(mat, j))

if __name__ == "__main__":
    main()
