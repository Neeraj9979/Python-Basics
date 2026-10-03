i=1
while(i<=10):
    if(i%2==0):
        i+=1
        continue
    else:
        print(i)
        i+=1

#This is beacause after continue the i value is stopped at 1 only it is not incrementing
#It is just stopped at 1 after incrementing the i=2 then checked if condition then skipped
#but i value is still 1
#So we need to increment after continue increment no use so before we have to increment