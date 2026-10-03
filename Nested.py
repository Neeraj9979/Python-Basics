Car=input("Enter Your Car:")
Car_Type=input("Enter your Cartype:")
if(Car=="BMW"):
    if(Car_Type=="M5"):
        print("Welcome to the Club")#Nested if is used when first if is true then comes to second if
    else:
        print("Not this time")
else:
    print("Sorry! you are not allowed")