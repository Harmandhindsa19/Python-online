#print the taken input to screen
l=[]
for x in range(10):
        l.append(int(input("enter the element:")))
print(l)

#infinite loop
x=10
while True:
    print("hello world")
    x+=1

#list
list=[]
for i in range(6):
        list.append(int(input("enter the element:")))
squarelist=[]
for i in range(6):
        squarelist.append(list[i]*list[i])
print(list)
print(squarelist)

# From a list containing ints, strings and floats,
# make three lists to store them separately.

list=[1,5.5,'izmir',70,40,'ali','bella','cow','denzili',8,2.2]
x=[]
y=[]
z=[]
for i in list:
    if type(i)==int:
        x.append(i)
    elif type(i)==float:
        y.append(i)
    elif type(i)==str:
        z.append(i)
print(list)
print(x)
print(y)
print(z)

#Using range(1,101), make a list containing even and odd numbers.

even=[]
odd=[]
for x in range(1,101):
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print(even)
print(odd)

#print the star pattern
for x in range(10):
    print("*"*x)

#Create a user defined dictionary and get keys corresponding to the value using for loop.


dict={}
keys=""
value=""
for x in range(4):
     keys=str(input("enter the keys:"))
     values=str(input("enter the values:"))
     dict[keys]=values

print(dict)
for k in dict.keys():
    print(k,dict[k])

#Take inputs from user to make a list.
#Again take one input from user and search it in the list and delete that element,if found.
#Iterate over list using for loop.

list=[]
for i in range(6):
    list.append(str     (input("enter the element:")))
print(list)
name=str(input("enter the name:"))
for j in list:
    if j==name:
        list.remove(j)
print(list)










