#tuple
#tuple with different data types

tuple=(1,2.4,3,4,"a",6,9)
print("tuple is:",tuple)
len(tuple)
print("length of tuple is:",len(tuple))

#largest and smallest number in tuple
tuple=(44,55,0,29,67,88)
print("tuple is: ",tuple)
print("maximum number in tuple is:",max(tuple))
print("minimum number in tuple is:",min(tuple))

#product of all elements in tuple
tuple=(1,2,3,4,5)
s=1
print("tuple is:",tuple)
for a in tuple:
    s=s*a
print(s)

# #sets
# #difference b/w two sets
a={1,2,3,4,5,7}
b={6,7,8,9,7,2,3}
print("A :",a)
print("B :",b)
print("difference b/w two sets are:",a-b)
print("difference b/w two sets are:",b-a)

#comparison and intersection
a={1,2,3,4,5,7}
b={6,7,8,9,7,2,3}
if(a==b):
    print("sets are equal")
else:
    print("sets are unequal and intersection is:",a&b)

Dictionary
#storing name and roll number


a=(str(input("enter the name of first student")))
b=(str(input("enter the name of second student")))
c=(str(input("enter the name of third student")))
d=(str(input("enter the name of forth student")))
e=(str(input("enter the name of fifth student")))
f=(str(input("enter the name of sixth student")))
g=(str(input("enter the name of seventh student")))
h=(str(input("enter the name of eigth student")))
i=(str(input("enter the name of ninth student")))
j=(str(input("enter the name of tenth student")))
a1=(int(input("enter the marks of first student")))
b2=(int(input("enter the marks of second student")))
c3=(int(input("enter the marks of third student")))
d4=(int(input("enter the marks of forth student")))
e5=(int(input("enter the marks of fifth student")))
f6=(int(input("enter the marks of sixth student")))
g7=(int(input("enter the marks of seventh student")))
h8=(int(input("enter the marks of eigth student")))
i9=(int(input("enter the marks of ninth student")))
j0=(int(input("enter the marks of tenth student")))
dic={a:a1 , b:b2 , c:c3 , d:d4 , e: e5 , f:f6 , g:g7 , h:h8 , i:i9 , j:j0 }
print("dictionary is:",dic)

#sorting of dictionary
dic={a:a1 , b:b2 , c:c3 , d:d4 , e: e5 , f:f6 , g:g7 , h:h8 , i:i9 , j:j0 }
L=[a1,b2,c3,d4,e5,f6,g7,h8,i9,j0]
print(dic)
L.sort()
print(L)

#MISSISSIPPI
a="MISSISSIPPI"
A=a.count("M")
print(A)
B=a.count("I")
print(B)
C=a.count("S")
print(C)
D=a.count("P")
print(D)
DIC={"M":A,"I":B,"S":C,"P":D}
print(DIC)




