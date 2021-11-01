class Account:
    __UserId: int
    __Balance: float = 0

    def __init__(self, userid: int):
        self.__UserId = userid

    def setBalance(self, balance:float):
        self.__Balance = balance

    def getBalance(self) -> float:
        return self.__Balance

    def getUserId(self) -> int:
        return self.__UserId