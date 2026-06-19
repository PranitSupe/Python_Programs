##basic:

#Q1.Create a Student object and add a name attribute.

class Student:
    pass

s1=Student()

s1.name="Pranit"

#Q2.Create a Car object and add a brand attribute.


class Car:
    pass

c1=Car()

c1.brand="BMW"


#Q3.Create a Book object and add a title attribute.

class Book:
    pass

b1=Book()

b1.title="Power of Mind"


print("----------------------------------")


#Q4.Print an attribute value.

print(s1.name)
print(c1.brand)
print(b1.title)

print("----------------------------------")

#Q5.Modify an existing attribute value.


s1.name="Rahul"
c1.brand="Mahindra"
b1.title="Rich Dad Poor Dad"


print("----------------------------------")


#Q6.Create a Student object with:
#name ,age. Print both.


class Student:
    pass

s1=Student()

s1.name="Pranit"
s1.age=20

print(s1.name)
print(s1.age)

print("----------------------------------")


#Q7.Create a Product object with:
#name,price
#Print both.

class Product:
    pass

p1=Product()

p1.name="Shoes"
p1.price=800

print(p1.name)
print(p1.price)



print("----------------------------------")


#Q8.Create an Employee object with:
#name
#salary
#department
#Print all details.

class Employee:
    pass

e1=Employee()

e1.name="Rahul"
e1.salary=40000
e1.department="Account"

print(e1.name)
print(e1.salary)
print(e1.department)



print("----------------------------------")


#Q9.Create two Student objects with different names.
#Print both.

s1=Student()
s2=Student()

s1.name="Pranit"
s2.name="Ketan"

print(s1.name)
print(s2.name)

print("----------------------------------")



#Q10.Update multiple attributes of an object.
#Example:

s1=Student()

s1.name = "Pranit"
s1.age = 20

s1.name = "Rahul"
s1.age = 21

print(s1.name)
print(s1.age)

print("----------------------------------")


##Advanced (11–15)
#Q11.Create 5 Student objects with different names.
#Store them in a list.
#Print all names.


s1=Student()
s2=Student()
s3=Student()
s4=Student()
s5=Student()

s1.name="Pranit"
s2.name="Ketan"
s3.name="Mohan"
s4.name="Pratik"
s5.name="Karan"

print(s1.name)
print(s2.name)
print(s3.name)
print(s4.name)
print(s5.name)


print("-----------------------------------------")

#Q12.Take student name from user input and store it as an attribute.
#Example:

class Student:
    def __init__(self,name):
        self.name=name

    def display(self):
        print(f"name:{self.name}")

name=input("enter your name:")
s1=Student(name)
s1.display()


print("-----------------------------------------")


#Q13.Create 3 Employee objects.
# Store:
# name
# salary
# Calculate total salary of all employees.


class Employee:
   pass

e1=Employee()
e1.name="rajesh"
e1.salary=40000

e2=Employee()
e2.name="ramesh"
e2.salary=45000

e3=Employee()
e3.name="mohan"
e3.salary=45000

total_salary=e1.salary + e2.salary + e3.salary
print(f"total Salary:{total_salary}")


print("-----------------------------------------")


class Employee:
    total_salary = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate(self):
        Employee.total_salary = Employee.total_salary + self.salary
        
    def display(self):
        print(f"total salary: {Employee.total_salary}")
        

e1 = Employee("rahul", 40000)
e2 = Employee("mohan", 45000)
e3 = Employee("rohan", 35000)

e1.calculate()
e2.calculate()
e3.calculate()
e3.display()

print("-----------------------------------------")


# Q14.Create two Student objects.
# Compare their names.

# Example:

if (s1.name == s2.name):
    print("Same")
else:
    print("Different")

    
print("-----------------------------------------")


#Q15.Create a mini Student Record System.
#Store for each student:
#name,age,marks
#Store 3 students in a list and display all records.

list=[]

class Student:
    def __init__(self,name):
        self.name=name

    def store(self):
        list.append(self.name)

    def display(self):
        print(list)     


s1=Student("pranit")
s1.store()
s1.display()


print("-----------------------------------------")

class Student:
    pass

students = []

for i in range(3):

    s = Student()

    s.name = input("Enter Name: ")
    s.age = int(input("Enter Age: "))
    s.marks = float(input("Enter Marks: "))

    students.append(s)

print("\nStudent Records")

for student in students:
    print(
        s.name,
        s.age,
        s.marks)


