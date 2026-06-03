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
        
