nums=[]
for i in range(6):
    nums.append(i*i)
print(nums)

nums1=[i*i for i in range(6) if i%2!=0]
print(nums1)

nums2=[-1,-2,-3,4,5,6,7,-8,-9,-10]
nums2=[0 if i<0  else i for i in  nums2]
print(nums2)