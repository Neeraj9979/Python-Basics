class Bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance        # private

    def get_info(self):
        return self.__balance         #getter Note:Must use return because it is returning a value

    def set_info(self,newBalance):    #Setter
        self.__balance=newBalance


b1=Bankaccount("Neeraj",20000)

b1.set_info(30000)
print(b1.name,b1.get_info())