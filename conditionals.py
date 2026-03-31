name= input("What is your name? ")
age= int(input(f"What is your age, {name}? "))
print(f"{name} is {age} years old.")

if age >= 18:
	print(f"{name} is old enough to vote")
else:
	print(f"{name} is not old enough to vote")

#guess the correct number game
actual_number= 15
input_number= int(input("Choose a number: "))

if actual_number > input_number:
	print(f"Your guessed number is greater than the number")
elif actual_number < input_number:
	print(f"Your guessed number is less than the number")
else:
	print(f"Your got it right...")