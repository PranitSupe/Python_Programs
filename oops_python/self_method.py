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
