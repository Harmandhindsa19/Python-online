list=[2,3,4,5,6,7,8,9]
a = 0
b = 0
print("list is:", list)
for x in list:
    if(x%2==0):
        a=a+1
    elif(x%2!=0):
        b=b+1
print("the count for even values is:",a)
print("the count for odd values is:",b)


