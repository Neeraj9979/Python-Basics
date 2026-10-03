from abc import ABC,abstractmethod
class addition(ABC):
    @abstractmethod
    def add(self,a,b):
        pass

class basicaddition(addition):
    def add(self,a,b):
        self.a=a
        self.b=b
        return a+b

b=basicaddition()
print(b.add(5,5))