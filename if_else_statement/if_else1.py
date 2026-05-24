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

    
