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

# num=int(input("enter a num"))
# is_prime=True
# if num<=1:
#     is_prime=False
# else:
#     for i in range(2,num):
#         if num % i==0:
#             is_prime = False
#         break
# if is_prime:
#     print("Prime")
# else:
#     print("Not Prime")

# num=54321
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# print(rev)

# num=122
# rev=0
# org=num
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# if org == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# for i in range(1,6):
    
#     for j in range(i):
         
#          print("*",end="")
#     print()

# numbers = [10, 5, 10, 8, 7]
# largest=0
# sec_largest=0
# for num in numbers:
#     if num>largest:
#         sec_largest=largest
#         largest=num
#     elif num < largest and num> sec_largest:
#         sec_largest=num
# print(sec_largest)

## String

# text="Python Developer"
# print(text[0])
# print(text[7])
# print(text[0:6])

# text = "  hello python world  "

# print(text.strip().upper())
# print(text.strip().title())
# print(text.strip().lower())

# text = "hello python"
# v="aeiou"
# count=0
# for i in text:
#     if i in v:
#         count=count+1
# print(count)

# text = "python"
# print(text[::-1])

# text = "madam"
# rev=text[::-1]
# if rev == text:
#     print("Palindrome")
# else:
#     print("Not-Palindrome")

# text = "hello world"
# count=0
# for i in text:
#     count+=1
# print(count)

# text = "programming"
# count=0
# for i in text:
#     if i == "m":
#         count+=1
# print(count)

# text = "I love Python"
# result=text.replace(" ","")
# print(result)