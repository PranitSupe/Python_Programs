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


