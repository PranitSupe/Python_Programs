## while_loop:

#1. Print numbers from 1 to 10 using a while loop.

num=1
while(num<=10):
    print(num)
    num=num+1

print("----------------------------")

#2. Print numbers from 10 to 1.

num=10
while(num>=1):
    print(num)
    num=num-1

print("----------------------------")


#3. Print all even numbers from 1 to 10.

num=1
while(num<=10):
    if num%2==0:
        print(num)
    num=num+1

print("----------------------------")


#4. Print all odd numbers from 1 to 20.

num=1
while(num<=10):
    if num%2!=0:
        print(num)
    num=num+1


print("----------------------------")


#5. Find the sum of numbers from 1 to 100.

sum=0
num=1
while(num<=10):
    sum=sum+num
    num=num+1
print(sum)

print("----------------------------")

#6. Print your name 5 times.

name="Pranit"
num=1
while(num<=5):
    print(name)
    
print("----------------------------")

#7. Print the multiplication table of a given number.

num=int(input("enter a number:"))
i=1
while(i<=10):
    print(num,"X",i,"=",(num*i))
    i=i+1

print("----------------------------")

#8. Count the number of digits in a number.

number=input("enter a number:")
i=1
while(i<=len(number)-1):
    i=i+1
print("number of digit in number:",i)

print("----------------------------")

#9. Find the sum of digits of a number.

num = 123
sum = 0

while num > 0:
    rem = num % 10          # Extract the last digit
    sum =sum + rem      # Add it to the sum
    num = num // 10         # Remove the last digit
print("sum of digit:",sum)

number=input("enter a number:")
sum=0
for i in number:
    sum=sum+int(i)
print("sum of digit in number:",sum)


print("----------------------------")
#10. Reverse a number.

print("----------------------------")

#11. Check whether a number is a palindrome.

print("----------------------------")

#12. Find the factorial of a number.

print("----------------------------")

#13. Keep taking input until the user enters 0.

print("----------------------------")
