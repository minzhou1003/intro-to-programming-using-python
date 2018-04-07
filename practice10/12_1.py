# minzhou@bu.edu

import math

class GeometricObject:
    def __init__(self, color="green", filled = True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):
        return "color: " + self.__color + \
               " and filled: " + str(self.__filled)

class Triangle(GeometricObject):

    def __init__(self, side1=1.0, side2=1.0, side3=1.0):
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getSide1(self):
        return self.side1

    def getSide2(self):
        return self.side2

    def getSide3(self):
        return self.side3

    def getArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2.0
        return math.pow(s * (s - self.side1) * (s - self.side2) * (s - self.side3), 0.5)

    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return "Triangle: side1 = " + str(self.side1) + " side2 = " + \
               str(self.side2) + " side3 = " + str(self.side3)


def main():

    [side1, side2, side3] = list(map(float, input('Enter three sides of a triangle: ').split(',')))
    color_str = input('Enter a triangle color: ')
    isfilled = int(input('Is the triangle filled? 0/1: '))

    triangle = Triangle(side1, side2, side3)
    triangle.setColor(color_str)
    triangle.setFilled(isfilled)

    print(str(triangle))
    print('Area:', triangle.getArea())
    print('Perimeter:', triangle.getPerimeter())
    print('Color:', triangle.getColor())
    if triangle.isFilled():
        print('Is Filled: True')
    else:
        print('Is Filled: False')

if __name__ == '__main__':
    main()