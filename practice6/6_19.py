# minzhou@bu.edu

# Return true if point (x2, y2) is on the left side of the # directed line from (x0, y0) to (x1, y1)
def leftOfTheLine(x0, y0, x1, y1, x2, y2):

    return (x1-x0) * (y2-y0) - (x2-x0)*(y1-y0) > 0


# Return true if point (x2, y2) is on the same # line from (x0, y0) to (x1, y1)
def onTheSameLine(x0, y0, x1, y1, x2, y2):

    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) == 0


# Return true if point (x2, y2) is on the right side of the # directed line from (x0, y0) to (x1, y1)
def rightOfTheLine(x0, y0, x1, y1, x2, y2):

    return (x1-x0) * (y2-y0) - (x2-x0)*(y1-y0) < 0


# Return true if point (x2, y2) is on the
# line segment from (x0, y0) to (x1, y1)
def onTheLineSegment(x0, y0, x1, y1, x2, y2):

    position = (x1-x0) * (y2-y0) - (x2-x0)*(y1-y0)
    return position <= 0.0000000001 and ((x0 <= x2 and x2 <= x1) or (x0 >= x2 and x2 >= x1))


def main():

    points = list(map(float, input('Enter coordinates for the three points p0, p1, and p2: ').split(',')))

    if leftOfTheLine(points[0], points[1], points[2], points[3], points[4], points[5]):
        print('p2 is on the left side of the line from p0 to p1')
        return

    if onTheLineSegment(points[0], points[1], points[2], points[3], points[4], points[5]):
        print('p2 is on the line segment from p0 to p1')
        return

    if onTheSameLine(points[0], points[1], points[2], points[3], points[4], points[5]):
        print('p2 is on the same line from p0 to p1')
        return

    if rightOfTheLine(points[0], points[1], points[2], points[3], points[4], points[5]):
        print('p2 is on the right side of the line from p0 to p1')
        return

main()