##Short-hand if-else

#1 Even or Odd

num=int(input("enter a number:"))
print("even number") if num%2==0 else print("odd number")

#2 Positive or Negative

num=int(input("enter a number:"))
print("positive number") if num>0 else print("negative number")

#3 Eligible for Voting
age=int(input("enter your age:"))
print("eligible for voting") if age>=18 else print("not eligible for voting")


#4 Largest of Two Numbers
n1=int(input("enter num1:"))
n2=int(input("enter num2:"))

print("num1 is greater ") if n1>n2 else print("num2 is greater")

#5 Check Password
password = "python"
print("Correct") if password == "python" else print("Wrong")

