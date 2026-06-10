

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