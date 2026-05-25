##Conditional statements:

#1. Even or Odd:
num=int(input("enter a number:"))
if (num%2==0):
    print(num,"is an even number")
else:
    print(num,"is an odd number")

#2. Positive or Negative:

num=int(input("enter a number:"))
if (num>=0):
    print(num,"is a positive number")
else:
    print(num,"is a negative number")


#3. Eligible for Voting:

age=int(input("enter your age:")) 
if (age>=18):
    print("you are eligible for votting") 
else:
    print("you are not eligible for votting") 


#4. Largest of Two Numbers:

n1=int(input("enter a number:"))
n2=int(input("enter a number:")) 

if (n1>n2):
    print(n1,"is greater number")
else:
    print(n2,"is greater number")

#5 Pass or Fail

mark=int(input("enter a marks:"))

if (mark>40):
    print("you are passed")
else:
    print("you are failed")

#6 Divisible by 3

n1=int(input("enter a number:")) 

if (n1%3==0):
    print(n1,"is divisible by 3")
else:
    print(n1," is not divisible by 3")

#7 Check Password

password=input("enter a password:")

if (password=="pass@123"):
    print("login successful")
else:
    print("login failed")

#8 Compare Two Strings:

str1=input("enter a string1:")
str2=input("enter a string2:")

if(str1==str2):
    print("both strings are same")
else:
    print("both strings are different")


#9 Check Leap Year
year=int(input("enter a year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")

#10 Check Number is Zero or Not:
num=int(input("enter a number:"))

if(num==0):
    print(num,"is zero")
else:
    print(num,"is not zero")
    