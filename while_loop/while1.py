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

#10. Reverse a number. #***
num=123
rev = 0
while num > 0:
    last_digit = num % 10
    rev = (rev * 10) + last_digit
    num = num // 10
print("reversed number",rev)

print("----------------------------")

#11. Check whether a number is a palindrome.

num=123
orignal_num=num
rev = 0
while num > 0:
    last_digit = num % 10              #last_digit=3     #last_digit=2    #last_digit=1  
    rev = (rev * 10) + last_digit      #rev=3            #rev=32          #rev=321
    num = num // 10                    #num=12           #num=1           #num=0

if orignal_num==rev:
    print("number is pelindrome")
else:
    print("number is not pelindrome")



print("----------------------------")

#12. Find the factorial of a number.

fact=1
num=5
while(num>=1):
    fact=fact*num
    num=num-1
print("factorial is:",fact)


print("----------------------------")

#13. Keep taking input until the user enters 0.

num=int(input("enter a number:"))
print("number is:",num)

while(num!=0):
    num=int(input("enter a number:"))
    print("number is:",num)

print("----------------------------")

#14. Generate Fibonacci series up to N terms.


num=int(input("enter a number :"))
n1=0
n2=1
n=1
while(n<=num):
    print(n1)
    temp=n1
    n1=n2
    n2=temp+n2
    n=n+1

print("----------------------------")


