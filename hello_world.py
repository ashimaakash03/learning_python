print("Hello, World!")

#basics of strings
print("Learning Python")
print('This is also a valid string')
print("Today's weather is so nice...")
print('We can also use "quotes"')

#concatenation of string literals
print("My name is " + 'Ashim Aakash Roy')

#concatenation using variables
greeting= "Hello"
name= "Ashim Aakash Roy"
print(greeting+" "+name)

#concatenation using input function
greeting= "Hello"
name= input("Enter your name: ")
print(greeting+" "+name)

#variable typecheck using type method
print(type(greeting))
print(type(name))
# even if a numerical value is entered in the CLI for the name variable, it is automatically converted to str.
name= 8085
print(type(name))

# print("up "+name)
#Code on line 37 gives an error because we are trying to add string with an integer, which is not possible in Python. Gives a TypeError.

#Escape characters
splitString= 'Hi!\nMy name is Ashim Aakash Roy\nI\'m 28 years old'
anotherString= 'The\tPython\tprograms\tare\tin C:\\Music\\Python\tfolder'
print(splitString)
print(anotherString)
