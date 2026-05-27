## Nested if Statement

#1 Check Eligible for Scholarship

marks=int(input("enter marks:"))
income=int(input("enter income:"))

if marks>=80:
    if income<50000:
        print("eligible for scholarship")
else:
    print("not eligible for scholarship")
