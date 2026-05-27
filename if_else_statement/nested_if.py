## Nested if Statement

#1 Check Eligible for Scholarship

marks=int(input("enter marks:"))
income=int(input("enter income:"))

if marks>=80:
    if income<50000:
        print("eligible for scholarship")
else:
    print("not eligible for scholarship")


#2 Login System

uid=input("enter user id:")
password=input("enter password:")

if uid=="UserName":
    if password=="Pass@123":
        print("login Successful")
print("Login Failed")
