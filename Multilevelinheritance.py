class employee:
    start="10Am"
    stop="5Pm"

class Adminstaff(employee):
    def __init__(self,role):
        self.role=role

class accountant(Adminstaff):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary=salary

acc1=accountant(200000,"CA")
print(acc1.role,acc1.salary,acc1.start,acc1.stop)


