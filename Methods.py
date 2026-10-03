class laptop:
    storage_type="ssd"

    def __init__(self,Pro,Ram,Rom): #instance method has self and it can access both class and instance attributes
        self.Pro=Pro
        self.Ram=Ram
        self.Rom=Rom

    def get_info(self):
        print(f"The Laptop l1 has {self.Pro} Processor {self.Ram} & {self.Rom} & {laptop.storage_type}")

l1=laptop("AMD Rhyzen","16Gb","512Gb")
l1.get_info()
