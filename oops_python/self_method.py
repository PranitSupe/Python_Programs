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
