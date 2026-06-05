## for loop:

#1 Print numbers from 1 to 10.

for i in range(1,11):
    print(i)


#2. Print numbers from 10 to 1.
 
for i in range(10,0,-1):
    print(i)


#3. Print your name 5 times using a loop.
for i in range(5):
    print("pranit")


#4. Print all even numbers from 1 to 20:
for i in range(1,21):
    if i%2==0:
        print(i)

#5. Print all odd numbers from 1 to 20.
for i in range(1,21):
    if i%2!=0:
        print(i)

#6 Find the sum of numbers from 1 to 100.

sum=0
for j in range(1,101):
    sum=sum+j
print("sum of numbers from 1 to 100 :",sum)

#7 Print the multiplication table of a number.
num=int(input("enter a number:"))
print("Table of", num,":")

for i in range(1,11):   
    print(num,"X",i,"=",num*i)


#8 Count how many numbers are divisible by 3 between 1 and 100.

count=0
for i in range(1,101):
    if i%3==0:
        count=count+1
print("numbers divisible by 3 between 1 and 100:",count)


#9 Calculate the factorial of a number.

fact=1
num=int(input("enter a number:"))
for i in range(1,num+1):
    fact=fact*i
print("factorial of ",num,"is:",fact)

#10 Find the sum of all even numbers from 1 to N.

num=int(input("enter a number:"))
sum1=0
for i in range(num+1):
    if i%2==0:
        sum1=sum1+i

print("sum=",sum1)

#11. Find the sum of all odd numbers from 1 to N.


num2=int(input("enter a number:"))
sum=0
for i in range(num2+1):
    if i%2!=0:
        sum=sum+i

print("sum=",sum)


#12. Reverse a string using a for loop.

str=input("enter a string:")
str2=""
for i in str:
    str2= i + str2
print(str2)

#13. Count vowels in a string.


str=input("enter a string:")
count=0
for i in str:
    if i in "aeiouAEIOU":
        count=count+1
print("count of vowels in a string: ",count)

#14. Print the Fibonacci series for N terms.

num=int(input("enter a number :"))
n1=0
n2=1
for i in range(num+1):
    print(n1)
    temp=n1
    n1=n2
    n2=temp+n2
#15 Check whether a number is prime.

num=int(input("enter a number:"))
flag=0

if (num<=1):
    print("not prime")
    flag=1
else:
    for i in range(2,num):
        if(num%i==0):
            print(" not prime")
            flag=1
            break

if (flag!=1):
    print("prime")


#16. Find all prime numbers between 1 and 100.


for num in range(1,20):
    flag=0
    if (num<=1):
        flag=1
        continue
    else:
        for i in range(2,num):
            if(num%i==0):
                flag=1
                break
    
    if (flag!=1):
        print(num)



#17. Print this pattern:
# *
# **
# ***
# ****
# *****

for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()



#18. Print this pattern:
#1
#12
#123
#1234
#12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()



#19. Find the largest number in a list without using max().

list=[1,2,8,4,5,6]
max=0

for i in list:
    if i>max:
        max=i
    else:
        max=max
print("maximum:",max)



#20. Find the second largest number in a list.
list=[19,2,18,4,5,6]

largest=0
second_largest=0

for i in list:
    if i > largest:
        second_largest=largest
        largest=i
    elif i > second_largest:
        second_largest=i

print("Second largest:",second_largest)




