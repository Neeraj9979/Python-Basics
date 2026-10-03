username=input("Enter your Username:")
password=input("Enter your password:")
if(username=="Admin" and password=="pass"):
    print("Login Successful!")
elif(username=="Admin" and password!="pass"):
    print("Wrong Password")
elif(username!="Admin" and password=="pass"):
    print("Wrong Username")
else:
    print("Wrong Username & Password")

