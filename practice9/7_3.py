# minzhou@bu.edu


class Account:

    def __init__(self, id = 0, balance = 100.0, annualInterestRate = 0.0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    # getter
    def getId(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    # setter
    def setId(self, n):
        self.__id = n

    def setBalance(self, n):
        self.__balance = n

    def setAnnualInterestRate(self, n):
        self.__annualInterestRate = n

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 1200

    def getMonthlyInterest(self):
        return self.getMonthlyInterestRate() * self.__balance

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

def main():

    account = Account(id=1122, balance=20000, annualInterestRate=4.5)
    account.withdraw(2500)
    account.deposit(3000)
    print('The account id: {}'.format(account.getId()))
    print('The account balance: {}'.format(account.getBalance()))
    print('The account monthly interest rate: {}'.format(account.getMonthlyInterestRate()))
    print('The account monthly interest: {}'.format(account.getMonthlyInterest()))

if __name__ == '__main__':
    main()