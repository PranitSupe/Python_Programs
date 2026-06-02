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




