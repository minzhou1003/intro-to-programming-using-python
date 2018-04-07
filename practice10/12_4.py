# minzhou@bu.edu


class Rectangle2D:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

    def containsPoint(self, x, y):
        return abs(x - self.x) <= self.width/2 and abs(y - self.y) <= self.height/2

    def contains(self, other):
        return ((self.x <= other.x ) and (self.x <= self.width)) \
               and ((other.x + other.width) <= (self.x + self.width)) \
               and ((other.y + other.height) <= (self.y + self.height))

    def overlaps(self, other):
        return not(self.x <= other.x  or self.x <= self.width \
               or ((other.x + other.width) <= (self.x + self.width)) \
               or ((other.y + other.height) <= (self.y + self.height)))

    def __contains__(self, other):
        return ((self.x >= other.x) and (self.y >= other.y)) \
               and ((other.x + other.width) >= (self.x + self.width)) \
               and ((other.y + other.height) >= (self.y + self.height))

    def __cmp__(self, other):
        if self.getArea() > other.getArea():
            return 1
        elif self.getArea() < other.getArea():
            return -1
        else:
            return 0

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __ne__(self, other):
        return self.__cmp__(other) != 0

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0


def getRectangle(points):
    xVals = [float(points[x]) for x in range(len(points)) if x % 2 == 0]
    yVals = [float(points[y]) for y in range(len(points)) if y % 2 != 0]
    xMax, yMax, xMin, yMin = max(xVals), max(yVals), min(xVals), min(yVals)
    x = (xMax + xMin) / 2
    y = (yMax + yMin) / 2

    return Rectangle2D(x, y, abs(xMax - xMin), abs(yMax - yMin))


def main():
    points = input('Enter the points: ')
    rect = getRectangle(points.split())
    print ('The bounding rectangle is centered at (%0.2f, %0.2f) with width %0.2f and height %0.2f' \
            % (rect.getX(), rect.getY(), rect.getWidth(), rect.getHeight()))

if __name__ == '__main__':
    main()