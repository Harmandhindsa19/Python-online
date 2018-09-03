#leap year
year=int(input("Enter the year: "))
if(year%4==0 and year%400!=0 and year%100!=0):
    print("the entered year is a leap year")
elif(year%4!=0 and year%400==0 and year%100==0):
    print("the entered year is a leap year")
elif(year%4==0 and year%400==0 and year%100==0):
    print("the entered year is a leap year")
else:
    print("the entered year is not a leap year")

#square and rectangle
length=int(input("enter the length of box:"))
breadth=int(input("enter the breadth of box:"))
if(length==breadth):
    print("the box is of square shape")
else:
    print("the box is of rectangle shape")

#oldest and yongest
person1=int(input("enter your age:"))
person2=int(input("enter your age:"))
person3=int(input("enter your age:"))
if(person1>person2>person3):
    print("person 3 is youngest and person 1 is eldest")
elif(person1<person2<person3):
    print("person 1 is youngest and person 3 is eldest")
elif(person2<person3<person1):
    print("person 2 is youngest and person 1 is eldest")
elif(person3<person1<person2):
    print("person 3 is youngest and person 2 is eldest")
elif(person1==person2==person3):
    print("all are having same age!")

#prize distribution
points=int(input("enter the points you get:"))
if(points>180 and points<=200):
    print("congratulation! you got choclates in prize")
elif(points>150 and points<=180):
    print("congratulation! you got a book in prize")
elif(points>50 and points<=150):
    print("congratulation! you got a wooden dog in prize")
elif(points>0 and points<=50):
    print("better luck next time, no prize")
else:
    print("points more than 200 are not applicable")

#discount prize
quantity=int(input("enter the quantity you have purchased:"))
cost=quantity*100
if(cost>1000):
    discount=cost*0.10
    totalcost=cost-discount
    print("your total cost after discount is:",totalcost)
else:
   print("your cost is:",cost)