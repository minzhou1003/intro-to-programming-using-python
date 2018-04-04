# minzhou@bu.edu

class LinearEquation:

    def __init__(self,a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    # getter
    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getD(self):
        return self.__d

    def getE(self):
        return self.__e

    def getF(self):
        return self.__f

    def isSolvable(self):
        return self.getA()*self.getD() - self.getB()*self.getC() != 0

    def getX(self):
        return (self.getE()*self.getD()-self.getB()*self.getF())/(self.getA()*self.getD()-self.getB()*self.getC())

    def getY(self):
        return (self.getA()*self.getF()-self.getE()*self.getC())/(self.getA()*self.getD()-self.getB()*self.getC())


def main():

    [a, b, c, d, e, f] = list(map(float, input('Enter a, b, c, d, e, f: ').split(',')))
    equation = LinearEquation(a, b, c, d, e, f)
    if equation.isSolvable():
        print('x is {} and y is {}'.format(equation.getX(), equation.getY()))
    else:
        print('The equation has no solution')


if __name__ == '__main__':
    main()