#data type conversion
a = 10
b = float(a)

print(b)
print(type(b))

print("-------------------------")

a = 10.8
b = int(a)

print(b)
print(type(b))

print("-------------------------")

num = 100
text = str(num)

print(text)
print(type(text))

print("-------------------------")

text = "50"
num = int(text)

print(num)
print(type(num))

print("-------------------------")

my_list = [1, 2, 3]

print(my_list)
print(type(my_list))

print("-------------------------")

my_tuple = (1, 2, 3)
print(type(my_tuple))

print("-------------------------")

my_set = {1, 2, 3}
print(type(my_set))

print("-------------------------")

student = {
    "name": "Pranit",
    "age": 20
}

print(type(student))

print("-------------------------")

value = input("Enter something: ")
print(type(value))

print("-------------------------")