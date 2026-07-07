# Q1.Create a Student class with:
# Instance Variable → name
# Class Variable → college = "Modern College"
# Print both.


print("=======================================")

class Student:
    college = "Modern College"

    def __init__(self,name):
        self.name=name
        print(f"Name:{self.name}")
        print(f"College:{Student.college}")

s1=Student("Rahul More")

print("=======================================")
    

# Q2.Create an Employee class.
# Instance Variable:
# employee_name
# Class Variable:
# company = "TCS"


class Employee:
    company = "TCS"

    def __init__(self,employee_name):
        self.employee_name=employee_name
        print(f"Employee Name:{self.employee_name}")
        print(f"Company:{Employee.company}")

s1=Employee("Ketan wagh")

print("=======================================")


# Q3.Create a Mobile class.
# Instance Variable:
# model
# Class Variable:
# brand = "Samsung"

class Mobile:
    brand = "Samsung"

    def __init__(self,model): 
        self.model=model 
        print(f"Model Name:{self.model}")
        print(f"Brand:{Mobile.brand}")

s1=Mobile("Samsung Galaxy S20")


print("=======================================")



# Q4.Create a Car class.
# Instance Variable:
# color
# Class Variable:
# wheels = 4


class Car:
    wheels = 4

    def __init__(self,color): 
        self.color=color 
        print(f"Car Color:{self.color}")
        print(f"No of wheels:{Car.wheels}")

c1=Car("RED")


print("=======================================")


# Q5.Create a Book class.
# Instance Variable:
# title
# Class Variable:
# language = "English"


class Book:
    language = "English"

    def __init__(self,title): 
        self.title=title 
        print(f"Book title:{self.title}")
        print(f"Language:{Book.language}")

b1=Book("Rich Dad Poor Dad")


print("=======================================")



# Intermediate (6–10)
