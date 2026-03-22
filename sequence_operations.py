string1= "My name is "
my_name= "Ashim Aakash Roy. "
what_i_do= "I study Python3."
print(string1+my_name+what_i_do)
print("Hello "*5)
# print("Hello " * 5 +4) gives error
print("Hello " * (5+4)) #prints Hello 9 times
print("Hello " * 5 + "4") #prints Hello 5 times followed by a 4. No error since 4 is of the type str

#To check if a big string consists a small string. Returns true if present. Otherwise, returns false.
today= "sunday"
print("sun" in today)
print("day" in today)
print("sat" in today)
print("Ashim " in my_name)

age= 28
print("My age is "+str(age)+" years old.") #Type coercion: force int to str
print("My age is {0} years old.".format(age)) #No type coercion. Recommended approach
#Another example
print("Days of the week: {0}, {1}, {2}, {3}, {4}, {5}, {6}"
      .format("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"))
