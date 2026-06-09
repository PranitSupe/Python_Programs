

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


#17. Find the product of all digits in a number.