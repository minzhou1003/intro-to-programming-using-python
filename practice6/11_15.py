# minzhou@bu.edu

def sameLine(points):

    x0, y0, x1, y1, x2, y2 = points[0], points[1], points[2], points[3], points[4], points[5]
    x3, y3, x4, y4 = points[6], points[7], points[8], points[9]

    if (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) == 0:
        if (x1 - x0) * (y3 - y0) - (x3 - x0) * (y1 - y0) == 0:
            if (x1 - x0) * (y4 - y0) - (x4 - x0) * (y1 - y0) == 0:
                return True
    return False


def main():
    points = list(map(float, input('Enter five points: ').split()))
    if sameLine(points):
        print('The five points are on the same line')
    else:
        print('The five points are not on the same line')


main()