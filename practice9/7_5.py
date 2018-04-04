# minzhou@bu.edu

import math

class RegularPolygon:

    def __init__(self, n = 3, side = 1, x = 0, y = 0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    # getter
    def getN(self):
        return self.__n

    def getSide(self):
        return self.__side

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    # setter
    def setN(self, n):
        self.__n = n

    def setSide(self, side):
        self.__side = side

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getPerimeter(self):
        return self.getSide()*self.getN()

    def getArea(self):
        return (self.getN()*(self.getSide()**2))/(4*(math.tan(math.pi/self.getN())))

def main():

    polygonOne = RegularPolygon(6, 4)
    polygonTwo = RegularPolygon(10, 4, 5.6, 7.8)
    print('RegularPolygon(6, 4)   perimeter: {}   area: {}'.format(polygonOne.getPerimeter(), polygonOne.getArea()))
    print('RegularPolygon(10, 4, 5.6, 7.8)   perimeter: {}   area: {}'.format(polygonTwo.getPerimeter(), polygonTwo.getArea()))

if __name__ == '__main__':
    main()