from main import *
class MegaHuman(SuperHuman):
    def __str__(self) -> str:
        return f"{self.name}, {self.age}, {self.wings}"
# hum3 = MegaHuman("askhat", 18)
# hum3.flying()
# print(hum3.fly())
class Bank:
    def __init__(self,name,age,balance,key) -> None:
        self.name = name
        self.age = age
        self._monye = balance
        self.__k = key
    def __str__(self) -> str:
        return f"{self.name}, {self.age}"
    def password(self):
        if len(self.__k) >= 8:
            return f"Ваш пароль сохранен, Ваш пароль: {self.__k}"
        else:
            return f"ваш пароль слишком легок"
bank = Bank("asyl", 16,1000, "sdfghjkvb")
print(bank)
print(bank.password())
print(bank._Bank__k)
bank._Bank__k = "sdfghjklcvbnm"
print(bank._Bank__k)
