# minzhou@bu.edu


import math

class QuadraticEquation:

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    # getter
    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getDiscriminant(self):
        return (self.getB())**2 - 4*self.getA()*self.getC()

    def getRoot1(self):
        if self.getDiscriminant() >= 0:
            return (-self.getB() + math.sqrt(self.getDiscriminant()))/(2*self.getA())
        return 0

    def getRoot2(self):
        if self.getDiscriminant() >= 0:
            return (-self.getB() - math.sqrt(self.getDiscriminant()))/(2*self.getA())
        return 0

def main():

    [a, b, c] = list(map(float,input('Enter a, b, c: ').split(',')))
    q = QuadraticEquation(a, b, c)
    if q.getDiscriminant() > 0:
        print('The roots are {} and {}'.format(q.getRoot1(), q.getRoot2()))
    elif q.getDiscriminant() == 0:
        print('The root is {}'.format(q.getRoot1()))
    else:
        print('The equation has no real roots')


if __name__ == '__main__':
    main()