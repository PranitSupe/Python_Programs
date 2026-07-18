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

# Q4.Create a Vehicle class with:
#Instance variable: model
#Instance method: show_model()

# Q5.Create a College class with:
# Class variable: college_name
# Class method: display_college()

# Intermediate (6–10)
# Q6.