
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
rev = 0
while num > 0:
    last_digit = num % 10              #last_digit=3     #last_digit=2    #last_digit=1  
    rev = (rev * 10) + last_digit      #rev=3            #rev=32          #rev=321
    num = num // 10                    #num=12           #num=1           #num=0

if num==rev:
    print("number is pelindrome")
else:
    print("number is not pelindrome")



print("----------------------------")

#12. Find the factorial of a number.

print("----------------------------")

#13. Keep taking input until the user enters 0.

print("----------------------------")
