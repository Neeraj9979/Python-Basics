class student:
    def __init__(self,name,cgpa): #__init__ is a constructor and self is parameter which is used to create a example of class for each object
        self.name=name #There are two types of constructors default and parameterized
        self.cgpa=cgpa #Default means self parameterized means name,cgpa etc....

stu=student("Neeraj",8.622)
stu2=student("Ishwarya",10.000)
print(stu.name,stu.cgpa)
print()