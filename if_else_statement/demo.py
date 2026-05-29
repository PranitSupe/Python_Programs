#Online Shopping Discount

amount = int(input("Enter purchase amount: "))
member = input("Premium member? (yes/no): ")

if amount>=5000:
    if member == "yes":
        print("Extra Discount Applied")
    else:
        print("No Extra Discount Applied")
else:
    print("No Extra Discount Applied")