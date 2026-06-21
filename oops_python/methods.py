##methods:

#Q1.Create a class Student with method display() that prints:
#Hello Student

class Student:
    def display(self):
        print("Hello Student")

s1=Student()
s1.display()

print("------------------------------------------")


#Q2.Create a class Car with method start().
#Output: Car Started

class car:
    def start(self):
        print("car started")

c1=car()
c1.start()

print("------------------------------------------")

#Q3.Create a class Book with method show_title().
#Print any book title.

class Book:
    def show_title(self):
        print("Good Habits")

b1=Book()
b1.show_title()

print("------------------------------------------")



#Q4.Create a class Employee with method greet().
#Print:Welcome Employee

class Employee:
    def greet(self):
        print("Welcome Employee")

e1=Employee()
e1.greet()

print("------------------------------------------")


#Q5.Create a class Mobile with method ring().
#Print:Phone Ringing...

class Mobile:
    def ring(self):
        print("Phone Ringing...")

m1=Mobile()
m1.ring()

print("------------------------------------------")


#6.Create a Calculator class with method add().
#Print:10 + 20 = 30

class Calculator:
    def add(self):
        a=10
        b=20
        print(a+b)

c1=Calculator()
c1.add()

print("------------------------------------------")


#Q7.Create a Calculator class with methods:
#add()
#subtract()

a=40
b=20
class Calculator:

    def add(self):
        print("addition:",a+b)
    
    def sub(self):
        print("substraction:",a-b)

c1=Calculator()
c1.add()
c1.sub()


print("------------------------------------------")


# Q8.Create a Rectangle class with method area().
#Calculate area of:
length = 10
width = 5
class Rectangle:

    def area(self):
        print("area of rectangle:",length * width)


r1=Rectangle()
r1.area()

print("------------------------------------------")



#Q9.Create a Number class with method is_even().
#Check whether:20 is even.

num=20
class Number:
    def is_even(self):
        if num%2==0:
            print("number is even")
        else:
            print("number is odd")

n1=Number()
n1.is_even()

print("------------------------------------------")



#Q10.Create a Student class with methods:
#study()
#play()
#Call both methods.


class Student:

    def play(self):
        print("Student play cricket")
    
    def study(self):
        print("Student do study")

s1=Student()
s1.study()
s1.play()


print("------------------------------------------")


#Q11.Create a Calculator class with methods:
#add()
#subtract()
#multiply()
#divide()



print("------------------------------------------")





#Q12.Create a Bank class with methods:
#deposit()
#withdraw()
#check_balance()
#Use fixed values.

#Q13.Create a ShoppingCart class with methods:
#add_item()
#remove_item()
#show_cart()

#Use print statements only.

#Q14.Create a Library class with methods:
#issue_book()
#return_book()
#show_books()

#Q15.Create a StudentManagement class with methods:
#add_student()
#display_student()
#delete_student()
#Use simple print statements.