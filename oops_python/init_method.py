# Basic (1–5)
# Q1.Create a class Greeting.
# When an object is created, print:
# Welcome to Python OOP

class Greeting:
    def __init__(self):
        print(" Welcome to Python OOP")

g1=Greeting()



# Q2.Create a class Computer.
# Constructor should print:
# Computer object initialized

class Computer:
    def __init__(self):
        print(" Computer object initialized")

c1=Computer()




# Q3.Create a class Movie.
# Create three objects and observe how many times the constructor runs.

class Movie:
    def __init__(self):
        print("Movie object initialized")

m1=Movie()
m2=Movie()
m3=Movie()

# Q4.Create a class City.
# Constructor should print:
# Pune City Selected


class City:
    def __init__(self):
        print("Pune City Selected")

c1=City()


# Q5.Create a class Exam.
# Print the memory address of the current object inside the constructor.
# Hint:
# print(id(self))
# Intermediate (6–10)

class Exam:
    def __init__(self):
        print(id(self))

e1=Exam()


# Q6.Create a class Student.
# Constructor should accept:
# name
# Display:
# Student Name: Pranit

class Student:
    def __init__(self,name):
        print(f"Name:{name}")

s1=Student("pranit")



# Q7
# Create a class Vehicle.
# Accept: brand
# Print: Vehicle Brand: Honda

class Vehicle:
    def __init__(self,Brand):
        print(f"Brand:{Brand}")

v1=Vehicle("Honda")




# Q8
# Create a class Restaurant.
# Accept:
# restaurant_name
# city
# Display both values.

class Vehicle:
    def __init__(self,Brand):
        print(f"Brand:{Brand}")

v1=Vehicle("Honda")



# Q9
# Create a class Laptop.

# Accept:

# brand
# RAM

# Create 3 laptop objects with different configurations.

# Q10

# Create a class Book.

# Accept:

# title
# author
# price

# Display complete book details.