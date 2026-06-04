#17. Print this pattern:
# *
# **
# ***
# ****
# *****



#19. Find the largest number in a list without using max().

list=[1,2,8,4,5,6]
max=0

for i in list:
    if i>max:
        max=i
    else:
        max=max
print("maximum:",max)