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
    digit = num % 10          # Extract the last digit
    sum =sum + digit      # Add it to the sum
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
    digit = num % 10
    rev = (rev * 10) + digit
    num = num // 10
print("reversed number",rev)

print("----------------------------")

#11. Check whether a number is a palindrome.

num=123
orignal_num=num
rev = 0
while num > 0:
    digit = num % 10              #last_digit=3     #last_digit=2    #last_digit=1  
    rev = (rev * 10) + digit      #rev=3            #rev=32          #rev=321
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



#15. Check whether a number is an Armstrong number.

number = 153         
temp = number        
sum = 0 

n = len(str(number))

while (temp > 0):
    digit = temp % 10
    sum =sum + (digit ** n)
    temp = temp // 10

if sum == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

print("----------------------------")


#16. Find the largest digit in a number.

number = 153        
temp = number        
max=0

while (temp > 0):
    digit = temp % 10
    temp = temp // 10
    if digit>max:
        max=digit
    else:
        max=max

print("maximum number:",max)
print("----------------------")

#17. Find the product of all digits in a number


number = 553      
temp = number        
sum=0

while (temp > 0):
    digit = temp % 10
    sum=sum + digit
    temp = temp // 10
   

print("sum of digit:",sum)
print("----------------------")

#18. Create a menu-driven calculator that continues until the user chooses Exit.

while(1):
    print("-----------------------")
    n1=int(input("enter a number 1:"))
    n2=int(input("enter a number 2:"))
    print("-------Menu--------------")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Exit")
    print("-----------------------")
    
    print("enter an operation number (0-4):")
    op=input("")

    if (op=="1"):
        print("Addition:",n1+n2)
    elif (op=="2"):
        print("Substraction:",n1-n2)
    elif (op=="3"):
        print("Multiplication:",n1*n2)
    elif (op=="4"):
        print("Division:",n1/n2)
    elif (op=="0"):
        print("exit...")
        break
      
print("----------------------")
       













#19. Guess the secret number until the correct answer is entered.
#20. Simulate an ATM menu (Balance Check, Deposit, Withdraw, Exit).
