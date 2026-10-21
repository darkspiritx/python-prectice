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

#Q11. Reverse a Number

num=12345
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("Reversed number: ",rev)

#Q13. Check Prime Number

n=9
if n<2:
    print("Not Prime Number")
else:
    for i in range(2,n):
        if n%i==0:
            print("Not Prime number")
            break
        else:
            print("Prime Number")

# Q14. Find the Largest in a List
numbers = [12, 45, 7, 89, 23]
largest=numbers[0]
for i in numbers:
    if i> largest:
        largest=i
print(f"Larget Number: {largest}")

# Q15. Count Even and Odd Numbers
numbers = [2,5, 8]
even=0
odd=0
for i in numbers:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(f"Even: {even}")
print(f"Odd: {odd}")

#Q16. Count Positive and Negative Numbers
numbers = [10, -5, 8, -2, 0, 7, -3]
positive=0
negative=0

for i in numbers:
    if i > 0:
        positive+=1
    elif i<0:
        negative+=1
    


print(f"Positive: {positive} \n Negative: {negative}")

# Q17: Find the Smallest Number

numbers = [34, 12, 56, 7, 89, 3]
smallest=numbers[0]
for i in numbers:
    if i < smallest:
        smallest=i

#Q18. Count Occurrences of a Number

numbers = [5, 2, 5, 8, 5, 3, 2]
num=int(input("Enter Your number: "))
num1=num
count=0
for i in numbers:
    if i == num:
        count+=1
print(f" {num}\n Number {num1} Appears: {count} times ")

# Count a Specific Number
numbers = [10, 20, 10, 30, 10, 40, 20]
num=int(input("Enter Your Number"))
num1=num
count=0

if num == numbers:
     for i in num:
        if i == num:
         count+=1
if count>0:
    print(f"{num}\nNumber {num1} appears: {count} times")
else:
  print("Number not found")

#I'm Mohit Prajapati

