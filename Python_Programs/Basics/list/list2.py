num=[2,3,4,5,6,7,8,9,10]
print("orignal list: ",num)


num.remove(10)
print("list after remove(10):",num)

num.pop()
print("list after pop():",num)


del num[0]
print("list after deleting index[0]:",num)



print("index of element(6):",num.index(6))

num.sort()
print("list after sorting(asc):",num)

num.sort(reverse=True)
print("list after sorting(desc):",num)


print("length of list:",len(num))

total=sum(num)
print("sum of list items:",total)


c=['d1','d2','d3']
print(" list before clear:",c)
c.clear()
print(" list after clear:",c)