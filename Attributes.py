class student:
    clg_name="Sr University"      #Class Attributes for whole class which will be common
    Branch="CSE(AIML)"
    def __init__(self,name,cgpa): #instance Attributes only for self objects which will be unique
        self.name=name
        self.cgpa=cgpa

stu1=student("Neeraj",8.622)
print(stu1.clg_name,student.Branch,stu1.name,stu1.cgpa)