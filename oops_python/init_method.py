# Basic (1–5)
# Q1.Create a class Greeting.
# When an object is created, print:
# Welcome to Python OOP

class Greeting:
    def __init__(self):
        print(" Welcome to Python OOP")

g1=Greeting()

print("=====================================")

# Q2.Create a class Computer.
# Constructor should print:
# Computer object initialized

class Computer:
    def __init__(self):
        print(" Computer object initialized")

c1=Computer()



print("=====================================")

# Q3.Create a class Movie.
# Create three objects and observe how many times the constructor runs.

class Movie:
    def __init__(self):
        print("Movie object initialized")

m1=Movie()
m2=Movie()
m3=Movie()


print("=====================================")

# Q4.Create a class City.
# Constructor should print:
# Pune City Selected


class City:
    def __init__(self):
        print("Pune City Selected")

c1=City()

print("=====================================")

# Q5.Create a class Exam.
# Print the memory address of the current object inside the constructor.
# Hint:
# print(id(self))
# Intermediate (6–10)

class Exam:
    def __init__(self):
        print(id(self))

e1=Exam()

print("=====================================")

# Q6.Create a class Student.
# Constructor should accept:
# name
# Display:
# Student Name: Pranit

class Student:
    def __init__(self,name):
        print(f"Name:{name}")

s1=Student("pranit")

print("=====================================")


# Q7
# Create a class Vehicle.
# Accept: brand
# Print: Vehicle Brand: Honda

class Vehicle:
    def __init__(self,Brand):
        print(f"Brand:{Brand}")

v1=Vehicle("Honda")


print("=====================================")


# Q8
# Create a class Restaurant.
# Accept:
# restaurant_name
# city
# Display both values.

class Restaurant:
    def __init__(self,restaurant_name,city):
        print(f"Restaurant name:{restaurant_name} , City: {city}")

r1=Restaurant("Panchali","Pune")


print("=====================================")

# Q9
# Create a class Laptop.
# Accept:
# brand
# RAM
# Create 3 laptop objects with different configurations.


class Laptop:
    def __init__(self,brand,RAM):
        print(f"Brand:{brand} , RAM: {RAM}")

l1=Laptop("Lenovo","8GB")
l2=Laptop("Apple","16GB")
l3=Laptop("Dell","8GB")


print("=====================================")

# Q10
# Create a class Book.
# Accept:
# title
# author
# price
# Display complete book details.

class book:
    def __init__(self,title,author,price):
        print(f"Title:{title} , Author: {author},Price: {price}")

b1=book("Good thoughts","Rajendra Singh", 450)


print("=====================================")

# Q11.Create a class CricketPlayer.
# Accept:
# player_name
# runs
# matches
# Create 5 players and display:
# Name | Runs | Matches

# Q12.Create a class ElectricityBill.
# Accept:
# customer_name
# units_consumed
# Calculate bill using:
# 1 unit = ₹8
# Display total amount.

# Q13.Create a class BankCustomer.
# Accept:
# name
# account_number
# balance
# Create multiple customers and display all details using a list.

# Q14.Create a class Product.
# Accept:
# product_name
# price
# Automatically calculate:
# GST = 18%
# Final Price = Price + GST
# inside the constructor.

# Q15.Create a class BusReservation.
# Accept:
# passenger_name
# seat_number
# destination
# Create 5 reservations and display all booking details.
