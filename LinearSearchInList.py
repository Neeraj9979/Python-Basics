# nums=[1,2,3,7,9,10]
# sk=7
# indx=0
# for i in nums:
#     if(i==sk):
#         print(f"{i} is found at the index value {indx}")
#         break
#     indx+=1

nums = [1,1,2,3,4,1,5,6,7,8,9,10]
sk = int(input("Enter a number to Search:"))
count=0
index=0
for i in nums:
    if(i==sk):
        print(f"{i} is found at the index:{index}")
        count+=1

    index+=1

    
print(count)