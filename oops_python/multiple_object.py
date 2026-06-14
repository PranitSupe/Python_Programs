##Basic (1–5)
#Q1.Create a class Student and create two objects.

class Student:
    pass

s1=Student()
s2=Student()

print("----------------------------------")

#Q2.Create a class Car and create three objects.

class Car:
    pass

c1=Car()
c2=Car()
c3=Car()


print("----------------------------------")

#Q3.Print all created objects.

print(c1)
print(c2)
print(c3)


print("----------------------------------")

#Q4.Print IDs of two Student objects.

print(id(c1))
print(id(c2))
print(id(c3))

print("----------------------------------")

#Q5.Check whether two objects have the same ID.

if (id(c1)==id(c2)):
    print("same")
else:
    print("not same")


print("----------------------------------")

##Intermediate (6–10)
#Q6.Create five objects of class Book.

class Book:
    pass

b1=Book()
b2=Book()
b3=Book()
b4=Book()
b5=Book()


print("----------------------------------")


#Q7.Store five objects in a list.

list=[]

for i in range(5):
    list.append(Book())

print(list)


print("----------------------------------")


#Q8.Loop through the list and print each object.

for i in list:
    print(i)

print("----------------------------------")

#Q9.Loop through the list and print IDs of all objects.

for i in list:
    print(id(i))

print("----------------------------------")


#Q10.Store objects inside a dictionary.

class Subject:
    pass

dict={
    "s1":Subject(),
    "s2":Subject(),
    "s3":Subject()
}