class laptop:
    company="Asus"

    @classmethod
    def get_info(cls):
        print(f"Comapany name is {laptop.company}") #cls is used and can access only class attributes

    def __init__(self,name,ram):
        self.name=name
        self.ram=ram

l1=laptop("Asus Rog","16gb")
l1.get_info()
print(l1.company)
print(l1.name,l1.ram)