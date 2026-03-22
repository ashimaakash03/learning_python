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
print("My age is "+str(age)+" years old.") # explicit type coercion: force int to str
print("My age is {0} years old.".format(age)) #No explicit type coercion. Recommended approach
#Another example
print("Days of the week: {0}, {1}, {2}, {3}, {4}, {5}, {6}"
      .format("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"))
#Another example
print("Jan: {0} days. Mar: {0} days, May: {0} days, Jul: {0} days, Aug: {0} days, Oct: {0} days, Dec: {0} days\n "
      "Apr: {1} days, June: {1} days, Sep: {1} days, Nov: {1} days"
      .format(31, 30)) #reusability

for num in range(1, 16):
      print("Number {0:2}, squared is {1:3}, cubed is {2:4}".format(num, num**2, num**3))
