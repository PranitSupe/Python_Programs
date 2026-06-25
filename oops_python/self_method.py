##SELF
# Basic (1–5)
# Q1.Create a method that prints self.

class greet:
    def to_greet(self):
        print(self)

g1=greet()
g1.to_greet()
    
print("------------------------------")

# Q2.Create a method that prints id(self).

class greet:
    def to_greet(self):
        print(id(self))

g1=greet()
g1.to_greet()


print("------------------------------")


# Q3.Create two objects and call the same method.

class Same:
    def meth1(self):
        print("method is called....")

s1=Same()
s1.meth1()

s2=Same()
s2.meth1()


print("------------------------------")


# Q4.Write a program without self and observe the error.


# class greet:
#     def to_greet():                      // error occur here
#         print("hello student.....")

# g1=greet()
# g1.to_greet()


print("------------------------------")


# Q5.Print id(s1) outside the class and id(self) inside the method.
# Compare them.
class greet:
    def to_greet(self):
        print(id(self))


g1=greet()
g1.to_greet()

print(id(g1))                      # both are same 



print("------------------------------")


# Q6.Create a method add_name() that stores:
# self.name = "Pranit"
# Print it.

class names:
    def add_name(self):
        self.name="Pranit"
        print(self.name)

n1=names()
n1.add_name()


print("------------------------------")


# Q7.Store:
# self.age = 20
# Print it.

class S_data:
    def add_data(self):
        self.name="Pranit"
        self.age=26
        print(" Name:",self.name," Age:",self.age)

n1=S_data()
n1.add_data()


print("------------------------------")

# Q8
# Store:
# self.city = "Pune"
# Print it.

class S_data:
    def add_data(self):
        self.name="Pranit"
        self.age=26
        self.city="Pune"
        print(" Name:",self.name," Age:",self.age," City:",self.city)

n1=S_data()
n1.add_data()


print("------------------------------")

# Q9
# Store three attributes using self:
# self.name
# self.age
# self.city
# Display all.

class Attributes:
    def store_data(self):
        self.name="Rahul"
        self.age=25
        self.city="Pune"
        print(" Name:",self.name," Age:",self.age," City:",self.city)

a1=Attributes()
a1.store_data()

print("------------------------------")


# Q10
# Create two Student objects.
# Store different names using self.
# Display both.

class Student:
    def add_name(self,name):
        self.name=name
        print("Name:",self.name)

s1=Student()
s2=Student()

s1.add_name("Kedar")
s2.add_name("Mohan")


print("------------------------------")



# Q11.Create a BankAccount class.
# Store:
# self.balance = 10000
# Display balance.


class BankAccount:
    def store_bal(self):
        self.balance=10000
    
    def display(self):
        print("Balence:",self.balance)

b1=BankAccount()
b1.store_bal()
b1.display()



# Q12.Create methods:
# deposit()
# withdraw()
# Modify:
# self.balance


class BankAccount:
    orignal_balnce=25000
    
    def deposit(self):
        self.Dep_balance=10000
        self.orignal_balnce=self.orignal_balnce + self.Dep_balance
    
    def withdraw(self):
        self.With_balance=10000
        self.orignal_balnce=self.orignal_balnce - self.With_balance
    
    def display(self):
        print("Balance:",self.orignal_balnce)


b1=BankAccount()
b1.deposit()
b1.display()
b1.withdraw()
b1.display()

# Q13.Create a Product class.
# Store:
# self.price
# Calculate a 10% discount.


# Q14.Create a StudentResult class.
# Store:
# self.name
# self.marks
# Display result.

# Q15.Create a Mini ATM System.
# Methods:
# deposit()
# withdraw()
# check_balance()
# Use:
# self.balance