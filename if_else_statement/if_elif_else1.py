##if-elif-else:

#1 Check Positive, Negative, or Zero

num=int(input("enter a number:"))

if(num>0):
    print(num,"is a positive number")
elif(num<0):
    print(num,"is a negative number")
else:
    print(num,"is zero")

#2 Find Largest of Three Numbers:

num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
num3=int(input("enter a number:"))

if(num1>num2 and num1>num3):
    print(num1,"is a greater number")
elif(num2>num1 and num2>num3):
    print(num2,"is a greater number")
else:
    print(num3,"is a greater number")

#3 Check Grade Based on Marks:


marks=int(input("enter marks:"))

if(marks>=80):
    print("Grade A")
elif(marks>=60 and marks<80):
    print("Grade B")
elif(marks>=40 and marks<60):
    print("grade C")
else:
    print("Grade D")