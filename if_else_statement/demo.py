# Exam Eligibility

attendance = int(input("Enter attendance percentage: "))
fees = input("Fees paid? (yes/no): ")

if attendance >= 75:
    if fees == "yes":
        print("Eligible for Exam")
    else:
        print("Not Eligible for Exam")
else:
    print("Not Eligible for Exam")
