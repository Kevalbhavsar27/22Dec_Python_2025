from abc import ABC,abstractmethod

class Account(ABC):

    balance = 0
    @abstractmethod
    def deposite(self,amount):
        pass

    @abstractmethod
    def withdrow(self,amount):
        pass

    def get_balance(self):
        print(f"current balance is {self.balance}")

class SavingAccount(Account):
    def deposite(self, amount):
        self.balance +=amount
    
    def withdrow(self, amount):
        if amount>self.balance:
           print("Insufficeint amount")
        else:
            self.balance-=amount


class LoanAccount(Account):
    def deposite(self, amount):
        if amount>self.balance:
            amt = amount-self.balance
            print(f"You have left {amt}")
            self.balance=0
        else:
            self.balance-=amount

    
    def withdrow(self, amount):
        self.balance+=amount
# saving  = SavingAccount()
# saving.get_balance()
# saving.deposite(5000)
# saving.deposite(2000)
# saving.get_balance()
# saving.withdrow(15000)
# saving.get_balance()

loan = LoanAccount()
loan.get_balance()
loan.withdrow(50000)
loan.get_balance()
loan.deposite(52000)
loan.get_balance()