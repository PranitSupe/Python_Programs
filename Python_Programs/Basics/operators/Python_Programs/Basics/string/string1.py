##1. Create a string with "Data Science" and print it

str1="Data Science"
print(str1)

##2. Print firsg and last character of the string "Machine learning"

str2="Machine learning"
print("First charecter: ",str2[0])
print("Second charecter: ",str2[-1])

##3. Find the length of the "Aritificial Intelligence"

str3="Aritificial Intelligence"
print("length of string: ",len(str3))

##4. given a string "data is widely available in the data world. without data, its very difficult. Data should be stored in data storage."
## find the occurance of word data

str4="data is widely available in the data world. without data, its very difficult. Data should be stored in data storage."
print("count of word 'data':",str4.count("data"))

##5. Check whether the string starts with"Py" in tghe string "Python is easy".

str5="Python is easy"
print(str5.startswith("Py"))


##6. print the string in reverse order - "Noddy is a cartoon"

str6="Noddy is a cartoon"
print(str6[-1::-1])


##7. remove the spaces from the string - "      I stay in Pune     "

str7="      I stay in Pune     "
print(str7.strip())