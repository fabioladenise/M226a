from  User import User

class AuthService:
    
    __users = []

    def __init__(self):
        self.__users.append(User(1, "user1", "user1"))
        self.__users.append(User(2, "user2", "user2"))
        self.__users.append(User(3, "user3", "user3"))

    def IsUserLoggedIn(self, userId: int) -> bool:
        for user in self.__users:
            if user.getId() == userId and user.isLoggedIn():
                return True
            return False

    def Login(self, un: str, pw: str) -> User:
        for user in self.__users:
            if user.getUsername() == un and user.getPassword() == pw:
                user.setLoggedIn(True)
                return user
            pass


    def Logout(self, un: str) -> bool:
        for user in self.__users:
            if user.getUsername() == un:
                user.setLoggedIn(False)
                return True
            return False
        
    
    def Logout(self, id: int) -> bool:
        for user in self.__users:
            if user.getId() == id:
                user.setLoggedIn(False)
                return True
            return False
        
    