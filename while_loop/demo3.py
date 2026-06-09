
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

#15. Check whether a number is an Armstrong number.


print("----------------------------")


#16. Find the largest digit in a number.


#17. Find the product of all digits in a number.