class Bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance         # public

b1=Bankaccount("Neeraj",20000)
print(b1.name,b1.balance)

class Bankaccount1:
    def __init__(self,name,balance):
        self.name=name
        self._balance=balance         # _protected

b2=Bankaccount1("Neeraj",20000)
print(b2.name,b2._balance)

class Bankaccount2:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance         # __private

    def get_info(self):
        print(self.__balance)
b3=Bankaccount2("Neeraj",20000)
print(b3.name,b3._Bankaccount2__balance)
b3.get_info()

