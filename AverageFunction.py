a=int(input("Enter number1:"))
# b=int(input("Enter number2:"))
# c=int(input("Enter number3:"))

def Average(a,b=1,c=1): #Note:The default values should be last not a the first
    avg=(a+b+c)/3
    return avg

print(Average(a))# A output statement should be able to work after a function