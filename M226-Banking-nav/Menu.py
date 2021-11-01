from User import User
from BankingService import BankingService
from AuthService import AuthService

class Menu:

    __user: User = None
    __auth: AuthService = None
    __bank: BankingService = None

    def __init__(self):
        self.__auth = AuthService()
        self.__bank = BankingService()
    

    def Run(self):
        while (True):
            if self.__user is None:
                self.__showWhenLoggedout()
            else:
                self.__showWhenLoggedIn()
            
    def __showWhenLoggedIn(self):
        while self.__user is not None:
            print("Bitte wählen sie:")
            print("k: Kontostand anzeigen")
            print("e: Einzahlen")
            print("a: Auszahlen")
            print("u: Überweisen")
            print("o: Ausloggen")
            print("x: Beenden")
            result: str = input()

            # Switch statements are more complicated in python. therefore we use if-elseif
            if result == "x":
                self.__exit()
            elif result == "k":
                self.__balance()
            elif result == "e":
                self.__deposit()
            elif result == "a":
                self.__withdraw()
            elif result == "u":
                self.__send()
            elif result == "o":
                self.__auth.Logout(self.__user.getId())
                self.__user = None
    
    def __balance(self):
    
        balance: float = self.__bank.getBalance(self.__user.getId())
        print("Dein Kontostand ist: " + str(balance))
    

    def __deposit(self):    
        amount: float = input("Wieviel Geld wird einbezahlt? CHF: ")
        self.__bank.deposit(self.__user.getId(), amount)
        print("Geld wurde einbezahlt")
        self.__balance()
    

    def __withdraw(self):
        done: bool = False
        while (not done):
            amount: float = input("Wieviel Geld wird abgehoben? CHF: ")
            try:
                self.__bank.withdraw(self.__user.getId(), amount)
                done = True            
            except Exception:
                print("Du hast nicht mehr so viel Geld!")
                self.__balance()
        print("Geld wurde abgehoben")
        self.__balance()
    

    def __send(self):
        done:bool = False
        id: int = input("An welche Benutzer-ID möchtests du Geld schicken? ID: ")
        while not done:
            amount: float = input("Wieviel Geld wird gesendet? CHF: ")
            try:
                self.__bank.sendMoney(self.__user.getId(), id, amount)
                done = True
            except Exception:
                print("Du hast nicht mehr so viel Geld!")
                self.__balance()
        print("Geld wurde geschickt")
        self.__balance()
    

    def __exit(self):
        print("Wir wünschen ihnen einen schönen tag")
        if (self.__user is not None):
            self.__auth.Logout(self.__user.getId())
        exit()
    

    def __showWhenLoggedout(self):
        while self.__user is None:
            print("Bitte wählen sie:")
            print("e: Einloggen")
            print("x: Beenden")
            result: str = input()

            if (result == "x"):
                self.__exit()
            elif (result == "e"):
                un: str = input("Geben sie den Benutzernamen ein: ")
                pw: str = input("Geben sie ihr passwort ein: ")
                self.__user = self.__auth.Login(un, pw)
    
