name= input("What is your name? ")
age= int(input(f"What is your age, {name}? "))
print(f"{name} is {age} years old.")

if age >= 18:
	print(f"{name} is old enough to vote")
else:
	print(f"{name} is not old enough to vote")