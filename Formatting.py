a=5
b=10
sum=a+b
print("Sum of",a,"and b",b,"is",sum)

#using format which is introdused in python 3.3
print("sum of {} and {} is {}".format(a,b,sum))
print("sum of {1} and {0} is {2}".format(a,b,sum))

#Using f-strings which are used in python 3.6
print(f"sum of {a} & {b} is {sum}")