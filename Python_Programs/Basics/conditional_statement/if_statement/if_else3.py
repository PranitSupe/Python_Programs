## if else Statement:

#1. Even or Odd

num=int(input("enter a number:"))
if num%2==0:
    print(num, "is a even number")
else:
    print(num ,"is a odd number")
    

print("-------------------------")

#2. Positive or Negative


num=int(input("enter a number:"))
if num>0:
    print(num, "is a positive number")
else:
    if num<0:
        print(num, "is a negative number")
    else:
        print(num, "is zero")


#3 Eligible for Voting :

age=int(input("enter age:"))
if age>=18:
    print("you ar eligibale for votting")
else:
    print("you are not eligible for voting")
    
print("----------------------")

#4 Largest of Two Numbers
#5 Pass or Fail