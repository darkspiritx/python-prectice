# # Find the oldest among 3 ages.
# age1=int(input("Enter First Age: "))
# age2=int(input("Enter Second Age: "))
# age3=int(input("Enter Third Age: "))

# if age1> age2 and age1>age3:
#     print("The Oldest Age is: ",age1)
# elif age2>age1 and age2>age3:
#     print("The Oldet Age is: ",age2)
# else:
#     print("The Oldest Age is: ",age3)

# #Convert celcius into fahrenhite.

# celcius = float(input("Enter Temprature in calcius: "))
# fahrenhite = (celcius*9/5)+32
# print("Temprature in Fahrenhite is: ",fahrenhite)

# #swap a number
# num1=int(input("Enter a First Number: "))
# num2=int(input("Enter a second Number: "))
# #without 3rd variable
# num1,num2 = num2,num1
# #with 3rd variable
# temp=num1
# num1=num2
# num2=temp
# print("===After Swap!===")
# print("First Number is: ",num1)
# print("Second Number is: ",num2)

# #Sum of three digit
# num=int(input("Enter 3 digit here!: "))

# digit1=num//100
# digit2=(num//10)%10
# digit3=num%10

# total=digit1+digit2+digit3

# print("Sum is: ",total)

# #Reverse number

# num=int(input("Enter 4 digit number here: "))
# original=num
# digit1=num%10
# digit2=(num//10)%10
# digit3=(num//100)%10
# digit4=(num//1000)
# reverse= digit1*1000 + digit2*100 + digit3*10 +digit4
# if reverse ==original:
#     print("Reverse Number is equal to original number.")
# else:
#     print("Reverse Number is not equal to original number.")

# #Leap Yaer

# year=int(input("Enter Year for check: "))
# if year % 400 ==0:
#     print("Leap Year")
# elif year % 100 ==0:
#     print("Not Leap Year")
# elif year % 4 ==0:
#     print("Leap Year")
# else:
#     print("Not Leap Year")

# #Find Eucliden Distance b/w 2 coordinate

# import math
# x1=float(input("Enter x1: "))
# y1=float(input("Enter y1: "))

# x2=float(input("Enter x2: "))
# y2=float(input("Enter y2: "))

# distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
# print("Eucliden Distance is: ",distance)

#Form of triangle

angle1=int(input("Enter First Angle: "))
angle2=int(input("Enter Second Angle: "))
angle3=int(input("Enter Third Angle: "))

if angle1 >0 and angle2 > 0 and angle3 > 0 and angle1 + angle2 + angle3 == 180:
    print("Triangle can be formeted.")
else:
    print("Triangle can not be formeted.")