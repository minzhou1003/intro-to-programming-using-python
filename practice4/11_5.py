# minzhou@bu.edu

def addMatrix(a, b):
    result = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    return result


def main():
    mat1 = list(map(float, input('Enter matrix1: ').split()))
    mat2 = list(map(float, input('Enter matrix2: ').split()))

    # Read input and save to two list of list
    row1 = mat1[0:3]
    row2 = mat1[3:6]
    row3 = mat1[6:]
    # print(row1, row2, row3)
    m1 = [row1]+[row2]+[row3]

    row1 = mat2[0:3]
    row2 = mat2[3:6]
    row3 = mat2[6:]
    # print(row1, row2, row3)
    m2 = [row1] + [row2] + [row3]

    res = addMatrix(m1, m2)

    # Print the result
    symb = [["   ", "   "], ["+  ", "=  "], ["   ", "   "]]
    print("The matrices are added as follows:")
    for i in range(len(m1)):
        print(str(m1[i][0]) + "   " + str(m1[i][1]) + "   " + str(m1[i][2]) + "   " + symb[i][0] + \
              str(m2[i][0]) + "   " + str(m2[i][1]) + "   " + str(m2[i][2]) + "   " + symb[i][1] + \
              str(res[i][0]) + "   " + str(res[i][1]) + "   " + str(res[i][2]))
              
main()


