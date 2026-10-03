from abc import ABC, abstractmethod
class animal(ABC):
    @abstractmethod 
    def sound(self):    #Abstraction only used for the blueprint that's it 
        pass

class lion(animal):
    def sound(self):
        print("Roar")
class cat(animal):
    def sound(self):
        print("meow")
class dog(animal):
    def sound(self):
        print("bark")

l1=lion()
c1=cat()
d1=dog()
l1.sound()
c1.sound()
d1.sound()
       
       
       
       
       