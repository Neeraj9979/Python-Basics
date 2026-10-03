class lion:
    def sound(self,arg):
        self.arg=arg
        print(f"The lion Roars {self.arg}")

class cat:
    def sound(self,arg):
        self.arg=arg
        print(f"The cat meows {self.arg}")

l1=lion()
c1=cat()
l1.sound("Heavily")
c1.sound("Silently")
