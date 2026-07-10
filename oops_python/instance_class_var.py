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

# Q6.Create three students with different names but the same college.
# Display all details.

class Student:
    college ="Modern College"

    def __init__(self,name):
        self.name=name
        print(f"Name:{self.name}, College:{Student.college}")

s1=Student("Rahul More")
s2=Student("Rohan Kedar")
s3=Student("Mohit Patil")

print("=======================================")


# Q7.Create four employees with different salaries but the same company.

class Employee:
    company ="TCS"

    def __init__(self,name):
        self.name=name
        print(f"Name:{self.name}, Company:{Employee.company}")

e1=Employee("Atul More")
e2=Employee("Kedar Kulkarni")
e3=Employee("Mohit Patil")

print("=======================================")


# Q8.Create five laptops with different RAM sizes but the same operating system.


class laptop:
    OS ="Windows 10"

    def __init__(self,RAM):
        self.RAM=RAM
        print(f"RAM:{self.RAM}, Company:{laptop.OS}")

l1=laptop("8GB")
l2=laptop("12GB")
l3=laptop("16GB")

print("=======================================")


# Q9.Create three products with different prices but the same GST percentage.


class product:
    GST ="18%"

    def __init__(self,price):
        self.price=price
        print(f"Price:{self.price}, Company:{product.GST}")

p1=product(2500)
p2=product(2000)
p3=product(1000)

print("=======================================")




# Q10.Create three buses with different bus numbers but the same route.



class bus:
    route ="Pune to MaNaPa"

    def __init__(self,bus_number):
        self.bus_number=bus_number
        print(f"Bus Number:{self.bus_number}, Route:{bus.route}")

b1=bus(121)
b2=bus(120)
b3=bus(122)

print("=======================================") 


# Advanced (11–15)

# Q11. Create a Hospital class.
# Instance Variables:
# patient_name
# age
# Class Variable:
# hospital_name = "City Hospital"
# Create 5 patients and display all details.




class Hospital:
   hospital_name = "City Hospital"

   def __init__(self,patient_name,age):
        self.patient_name=patient_name
        self.age=age
        print(f"Patient_name:{self.patient_name}, Age:{self.age}")

b1=Hospital("Mohan More",25)
b2=Hospital("Ketan Wagh",23)
b3=Hospital("Lokesh Patil",25)

print("=======================================") 


# Q12. Create a MovieTicket class.
# Instance Variables:
# customer_name
# seat_number
# Class Variable:
# theatre = "PVR Cinemas"
# Display ticket details.


class MovieTicket:
   theatre = "PVR Cinemas"

   def __init__(self,customer_name,seat_number):
        self.customer_name=customer_name
        self.seat_number=seat_number
        print(f"Customer_name:{self.customer_name}, Seat_number:{self.seat_number}")

b1=MovieTicket("Mohan More",2)
b2=MovieTicket("Ketan Wagh",3)
b3=MovieTicket("Lokesh Patil",5)

print("=======================================") 


# Q13. Create a LibraryBook class.
# Instance Variables:
# title
# author
# Class Variable:
# library_name = "Central Library"
# Create multiple books.

# Q14. Create a TrainReservation class.
# Instance Variables:
# passenger_name
# coach
# Class Variable:
# train_name = "Rajdhani Express"
# Create 4 reservations.


# Q15.Create a School class.
# Instance Variables:
# student_name
# standard
# percentage
# Class Variable:
# school_name = "ABC Public School"
# Create 5 students and display all information.

