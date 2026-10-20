#Q1. Add Two Numbers

num1=int(input("Enter a first number: "))
num2=int(input("Enter a second number: "))
print(f"Sum of two number is :{num1+num2}")

#Q2. Even or Odd

num=int(input("Enter a number: "))
if num%2==0:
    print("Even Number")
else:
    print ("Odd Number")

#Q3. Find the Largest Number

num1=int(input("Enter a first number"))
num2=int (input("Enter a second number"))
if num1>num2:
    print(f"Number first is Largest: {num1} ")
else:
    print (f"Number Second is Largest: {num2}")

#Q4. Print Numbers Using a Loop

for i in range(1,11):
    print(i)

#Q5. Sum of Numbers

n=int(input("Enter a number"))
total=0
for i in range (1,n+1):
    total=total+i
print(total)

#Q6. Positive, Negative or Zero

print("Check a Number is Positive, Negative or Zero")
n=int(input("Enter a number : "))
if n >0:
    print(f"Your enter number is postive: {n}")
elif n<0:
    print(f"Your enter number is Negative: {n}")
elif n==0:
    print(f"Your Enter Number is Zero: {n}")
else:
    print("Please Enter a Valid Number")

#Q7. Count from 1 to N
n=int(input("Enter a number"))
for i in range(1,n+1):
    print(i)

#Q8. Multiplication Table

n=int(input("Enter number for table"))
for i in range (1,11):
    print(f"{n}x{i}={n*i}")

#Q9. Sum of Even Numbers

total=0
for i in range(1,21):
    if i %2==0:
        total=total+i
print(total)

#Q10. Factorial of a Number

n=int(input("Enter a number for factorial: "))

total=1
for i in range (1,n+1):
    
 
    total=total*i
    
print(f"Your Factorial is: {total}")