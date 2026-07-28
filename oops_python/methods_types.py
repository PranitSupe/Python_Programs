# Basic (1–5)
# Q1.Create a Student class with an instance method show_name() that displays a student's name.

class Student:
    def __init__(self,name):
        self.name=name

    def show_name(self):
        print("student name is:",self.name)

s1=Student("Ravi")
s1.show_name()



# Q2.Create an Employee class with a class variable company = "Infosys" and a class method to display it.


class Employee:
    company = "Infosys"

    @classmethod
    def show_name(cls):
        print("company name is:",cls.company)

e1=Employee()
e1.show_name()

# Q3.Create a MathTools class with a static method that prints the square of 9.

class MathTools:

    @staticmethod
    def square():
        print("square of 9 is :",(9*9))

MathTools.square()


# Q4.Create a Vehicle class with:
#Instance variable: model
#Instance method: show_model()


class Vehicale:
    def __init__(self,model):
        self.model=model

    def show_model(self):
        print("model is :",self.model)

v1=Vehicale("BMW")
v1.show_model()

# Q5.Create a College class with:
# Class variable: college_name
# Class method: display_college()

class College:
    college_name="ABC college"

    @classmethod
    def display_college(cls):
        print("college name is:",cls.college_name)

c1=College()
c1.display_college()


# Intermediate (6–10)

# Q6.Create a Bank class with:
# Instance variable: account_holder
# Class variable: bank_name
# Instance method to display account holder
# Class method to display bank name


class Bank:
    bank_name="SBI"

    def __init__(self,account_holder):
        self.account_holder=account_holder

    def display_account_holder(self):
        print("account holder is :",self.account_holder)

    @classmethod
    def display_bank_name(cls):
        print("bank name is :",cls.bank_name)

b1=Bank("Raj")
b1.display_account_holder()
b1.display_bank_name()


# Q7.Create a Temperature class with a static method that converts Celsius to Fahrenheit.

class Temperature:

    @staticmethod
    def celcious_to_farenhite(c):
        f=(c*9/5)+32
        print("temperature in farenhite is:",f)

c1=Temperature()
c1.celcious_to_farenhite(40)


# Q8.Create a Product class with:
# Instance method to display product details
# Static method to calculate a 15% discount on a given price

class Product:
    def __init__(self,product_details):
        self.product_details=product_details

    def display_product(self):
        print("product details:",self.product_details)

    @staticmethod
    def discount(price):
        discount=price*0.15
        print("discounted price is:",discount)


p1=Product("mobile")
p1.display_product()
p1.discount(10000)



# Q9.Create a School class with:
# Class variable: school_name
# Instance variable: student_name
# One instance method and one class method

class School:
    school_name="shivaji school"

    def __init__(self,student_name):
        self.student_name=student_name

    def display_student_name(self):
        print("student name is:",self.student_name)

    @classmethod
    def display_school_name(cls):
        print("school name is:",cls.school_name)


# Q10.Create a Circle class with a static method
#  that calculates the area for a given radius.

