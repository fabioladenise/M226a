class User:
    __Id: int
    __Username: str
    __Password: str
    __IsLoggedIn: bool = False

    def __init__(self, id: int, user: str, pw: str):
        self.__Id = id
        self.__Username = user
        self.__Password = pw

    def setLoggedIn(self, newValue: bool):
        self.__IsLoggedIn = newValue

    def isLoggedIn(self) -> bool:
        return self.__IsLoggedIn

    def getId(self) -> int:
        return self.__Id

    def getUsername(self) -> str:
        return self.__Username

    def getPassword(self) -> str:
        return self.__Password