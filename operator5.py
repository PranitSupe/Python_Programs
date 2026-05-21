## Identity Operators

#1. Identity Operator (is):

a=[3,2,1]
b=a

print(a is b)
print("-------------------------")

#2. Identity Operator (is not)

a=[3,2,1]
b=[1,2,3]

print(a is not b)
print("-------------------------")

## Membership Operators:

#1 Membership Operator (in)
text="Python"

print("P" in text)
print("-------------------------")

#1 Membership Operator (not in)
text="Python"

print("z" not in text)
print("-------------------------")


## Bitwise Operators
#1. Bitwise AND 
a=5
b=3
print("a=",a)
print("b=",b)
print("Bitwise AND operation:",a & b)
print("-------------------------")

#2. Bitwise OR
a=5
b=3
print("a=",a)
print("b=",b)
print("Bitwise OR operation:",a | b)
print("-------------------------")

#3. Bitwise XOR
a=5
b=3
print("a=",a)
print("b=",b)
print("Bitwise XOR operation:",a ^ b)
print("-------------------------")