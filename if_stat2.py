## if Statement:

#1. Check Even Number

num=int(input("enter a number:"))
if num%2==0:
    print(num, "is a even number")

print("-------------------------")

#2 Check Password

password = input("enter password:")
if (password == "123"):
    print("password is correct")


print("-------------------------")

#3 Check Temperature
temp=int(input("enter temperature:"))
if temp>35:
    print("temperature is high")

print("-------------------------")

#4 Check Character is Alphabet

char=input("enter a character:")
if ((char>='a' and char<='z') or (char>='A' and char<='Z')):
    print(char, "is an alphabet") 
     

#5 Check Student Passed
