class laptop:
    company="Asus"

    @classmethod
    def get_info(cls):
        print(f"Comapany name is {laptop.company}") #cls is used and can access only class attributes

    def __init__(self,name,ram):
        self.name=name
        self.ram=ram

    @staticmethod
    def dis_price(price,discount): #Static methods are separate which do nat have access to class and insatance but related to them 
        final_price=price - (discount * price / 100)
        return final_price

l1=laptop("Asus Rog","16gb")
l1.get_info()
print(l1.name,l1.ram)
print(l1.dis_price(40000,10))