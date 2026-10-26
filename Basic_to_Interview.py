# # IF ELSE ELIF LOOP

# num=int(input("Enter a number"))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# num=int(input("Enter a number"))
# if num>0:
#     print("POSTIVE")
# elif num<0:
#     print("NEGATIVE")
# elif num==0:
#     print("ZERO")
# else:
#     print("INVALID NUMBER")

# num1=int(input("Enter a First number: "))
# num2=int(input("Enter a Second number: "))
# if num1>num2:
#     print("First number is Largest")
# elif num1<num2:
#     print("Second Number is Largest")
# else:
#     print("Both are equal")

# for i in range(1,10+1):
#     print(i)

# n=int(input("enter a number"))
# total=0
# for i in range(1,n+1):
#     total=total+i
# print(total)

# num=int(input("enter a number"))
# for i in range(1,11):
#     print(f"{num}x{i}={num*i}")

# num=int(input("enter number: "))
# total=0
# for i in range(1,num+1):
#     if i%2==0:
#         total=total+i
# print(total)

# num=int(input("enter a number"))
# count=0
# while num>0:
#     digit=num%10
#     count+=1
#     num=num//10

# print(count)

# n=int(input("enter a number"))
# result=1
# for i in range(1,n+1):
#     result=result*i
# print(result)

# for i in range(1,31):
#     if i%3==0 and i%5==0:
#            print("Fizz Buzz")  
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("buzz")
       
#     else:
#         print(i)

num=int(input("enter a num"))

for i in range(2,num-1):
    if num == 1:
        print("Not prime")
    elif num%i==0:
        print("Not prime")
else:
        print("Prime")
