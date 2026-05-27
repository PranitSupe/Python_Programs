## Nested if Statement

#1 Check Eligible for Scholarship

marks=int(input("enter marks:"))
income=int(input("enter income:"))

if marks>=80:
    if income<=50000:
        print("eligible for scholarship")
    else:
        print("not eligible for scholarship")
else:
    print("not eligible for scholarship")


#2 Login System

uid=input("enter user id:")
password=input("enter password:")

if uid=="UserName":
    if password=="Pass@123":
        print("login Successful")
    else:
        print("Login Failed")
else:
    print("Login Failed")

#3 Positive Even Number:

num=int(input("enter a number:"))

if num>0:
    if num%2==0:
        print(num,"is positive even number")
    else:
        print(num,"is positive number but not even")
else:
    print(num,"is neither even nor positive")