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





1
22
333
4444
55555
