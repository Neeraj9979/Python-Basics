f=open("R+,W+,A+.txt","r+") #We can read and write at the same but we can write a starting
f.write("143")
f.close()
f=open("R+,W+,A+.txt","a+") #We can append and write at the same but we can write a ending
f.write("143")
f.close()
f=open("R+,W+,A+.txt","w+") #Overwrites Everything
f.write("143")
f.close()  

