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
    list_account = []
    for i in range(10):
        list_account.append(Account(id=i, balance=100))
    while 1:
        try:
            enteredId = int(input('Enter an account id: '))
        except ValueError:
            print('Please enter a correct id')
            continue

        if enteredId > 10 or enteredId < 0:
            print('Please enter a correct id')
        else:
            while 1:
                print('Main menu')
                print('1: check balance')
                print('2: withdraw')
                print('3: deposit')
                print('4: exit')
                number = int(input('Enter a choice: '))

                if number == 1:
                    print('The balance is', list_account[enteredId].getBalance())
                    print()
                if number == 2:
                    amount = float(input('Enter an amount to withdraw: '))
                    list_account[enteredId].withdraw(amount)
                    print()
                if number == 3:
                    amount = float(input('Enter an amount to deposit: '))
                    list_account[enteredId].deposit(amount)
                    print()
                if number == 4:
                    print()
                    break


if __name__ == '__main__':
    main()