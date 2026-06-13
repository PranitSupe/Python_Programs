## Object:

#Q1. Create a class Student and create one object s1.

class Student:
    pass

s1=Student()


#Q2.Create a class Car and create one object c1.

class Car:
    pass

c1=Car()

#Q3.Create a class Book and create one object b1.

class Book:
    pass
b1=Book()

#Q4.Print the object s1.

class Student:
    pass

s1=Student()
print(s1)

print("----------------------------")

#Q5.Print the type of object s1.

class Student:
    pass

s1=Student()
print(type(s1))
print(Student)


print("----------------------------")

#Q6.Create two objects of class Student.
#s1 = Student()
#s2 = Student()
#Print both.

class Student:
    pass

s1=Student()
s2=Student()
print(s1)
print(s2)


print("----------------------------")

#Q7.Create three objects of class Car

class Car:
    pass

c1=Car()
c2=Car()
c3=Car()

print("----------------------------")

#Q8.Print memory addresses using:
print(id(s1))
print(id(s2))

print("----------------------------")

#Q9
#Check whether:
#s1 == s2
#returns True or False.

print(s1==s2)

print("----------------------------")

#Q10.Create objects of three different classes.

class A:
    pass

class B:
    pass

class C:
    pass

a1=A()
b1=B()
c1=C()

print(id(a1))
print(id(b1))
print(id(c1))

print("----------------------------")

##Advanced:

#Q11.Create five Student objects and store them in a list.

list=[]

class Student:
    pass

s1=Student()
s2=Student()
s3=Student()

list.append(s1)
list.append(s2)
list.append(s3)

print(list)


print("-------------------------------")

#Q12. Loop through the list and print each object

list=[s1,s2,s3]

for i in list:
    print(i)


print("-------------------------------")

#Q13.Print IDs of all objects.

list=[s1,s2,s3]

for i in list:
    print(id(i))


print("-------------------------------")

#Q14.Create a function that accepts an object as parameter.

def func(obj):
    print(obj)

list=[s1,s2,s3]
for i in list:
    func(i)

print("-------------------------------")

#Q15.Create 10 objects using a loop and store them in a list.

class loops:
    pass
list=[]

for i in range(5):
    list.append(Student())

print(list)

print("-------------------------------")