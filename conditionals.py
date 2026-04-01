name= input("What is your name? ")
age= int(input(f"What is your age, {name}? "))
print(f"{name} is {age} years old.")

# if age >= 18:
# 	print(f"{name} is old enough to vote")
# else:
# 	print(f"{name} is not old enough to vote")
#
# #guess the correct number game
# actual_number= 15
# input_number= int(input("Choose a number: "))
#
# if actual_number > input_number:
# 	print(f"Your guessed number is greater than the number")
# elif actual_number < input_number:
# 	print(f"Your guessed number is less than the number")
# else:
# 	print(f"Your got it right...")

#guess if person is allowed to work

#if age<=16 and age>=65
if 16 <= age <= 65:
	print(f"{name} is elligible to work")
else:
	print(f"{name} is not elligible to work")

if age<17 or age>66:
	print(f"{name} is not elligible to work")
else:
	print(f"{name} is elligible to work")

day= "Sunday"
temperature= 35
raining= True

if day == "Monday" and temperature > 27 and not raining:
	print(f"{day} is good to learn Python")
else:
	print(f"Go out on {day}")

# if 0:
# 	print("True") It is an unreachable code because 0 is always considered false
# else:
# 	print("False")

name= input("What is your name? ")
if name:
	print(f"Hello, {name}!")
else:
	print(f"Don't you have a name?")

parrot= "Norwegian Blue"
letter= input("Enter a character: ")
if letter in parrot:
	print(f"{letter} is in {parrot}")
else:
	print(f"{letter} is not in {parrot}")