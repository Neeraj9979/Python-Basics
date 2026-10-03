class employee:
    start="10Am"
    stop="5Am"

    def change_time(self,stoptime):
        self.stop=stoptime
class teacher(employee):
    def __init__(self,subject):
        self.subject=subject


t1=teacher("Math")
t1.change_time("6Am")
print(t1.subject,t1.start,t1.stop)

t2=teacher("Social")
print(t2.subject,t2.start,t2.stop)

