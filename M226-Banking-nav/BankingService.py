from AuthService import AuthService
from Account import Account

class BankingService:
    __accounts = []

    def __init__(self):
        self.__accounts.append(Account(1))
        self.__accounts.append(Account(2))
        self.__accounts.append(Account(3))
    

    def deposit(self,  userId: int, amount: float):
        account = self.__getAccount(userId)
        newBalance: float = float(account.getBalance()) + float(amount)
        account.setBalance(newBalance)
    

    def withdraw(self, userId: int, amount: float):
        account = self.__getAccount(userId)
        newBalance: float = float(account.getBalance()) - float(amount)
        if newBalance < 0:
            raise Exception("You don't have that much on your account")
        else:
            account.setBalance(newBalance)
        
    

    def getBalance(self, userId: int) -> float:
        return self.__getAccount(userId).getBalance()
    

    def sendMoney(self, fromId: int, to: int, amount: float):
    
        self.withdraw(fromId, amount)
        self.deposit(to, amount)
    

    def  __getAccount(self, userId: int) -> Account:
        for acc in self.__accounts:
            if acc.getUserId() == int(userId):
                return acc
        pass
        
    