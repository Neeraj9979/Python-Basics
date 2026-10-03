class teacher:
    def __init__(self,salary):
        self.salary=salary


class student:
    def __init__(self,cgpa):
        self.cgpa=cgpa

class TA(teacher,student):
    def __init__(self,name,salary,cgpa):
        super().__init__(salary)
        student.__init__(self,cgpa)
        self.name=name

T1=TA("Shradha",200000,9.3)
print(T1.name,T1.salary,T1.cgpa)