class animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print(f"The {self.name} have a heavy sound")

class cat(animal):
    def sound(self):
        print(f"The {self.name} type animal are having a low sound")

a1=animal("Lion")
ac1=cat("Cat")
a1.sound()
ac1.sound()