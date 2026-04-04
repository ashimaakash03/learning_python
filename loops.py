import random

iterable = "ASHIM AAKASH ROY"

for char in iterable:
	print(char.casefold())

#print all numbers from 1 to 20
for num in range(1, 21):
	print(f"Number is now {num}")

#print all even numbers from 1 to 20
for num in range(1, 21):
	if num % 2 == 0:
		print(f"Number {num} is even")
	else:
		print(f"The square of odd number {num} is {num ** 2}")
print()
#print all numbers from 1 to 20
#here we omitted the start value. Starts from 0 by default
for num in range(21):
	print(f"Number is now {num}")
print()
#Introducing the positive step value. If the step value is omitted, it is considered to be 1
for num in range(0,21, 2):
	print(f"Number is now {num}") # Output is 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20.
print()
#Since step value is 2
for num in range(0,21, 5):
	print(f"Number is now {num}")
print()
# Output is 0, 5, 10, 15, 20. Since step value is 5

#Introducing the negative step value. Start value is greater than stop value for negative step
for num in range(20,0, -2):
	print(f"Number is now {num}") # Output is 20, 18, 16, 14, 12, 10, 8, 6, 4, 2.
#Since step value is -2.
print()
for num in range(20,0, -5):
	print(f"Number is now {num}")
# Output is 20, 15, 10, 5. Since step value is -5.
print()

#Nested for loop
for num1 in range(1, 11):
	for num2 in range(1, 16):
		print(f"{num1} times {num2} are {num1 * num2}")
	print()
print()

#Demonstrate a simple while loop to print numbers 1 to 15
index = 1
while index in range(1, 16):
	print(f"Number is now {index:>2}")
	index += 1
print()

highest_limit= 15
correct_number= random.randint(1,highest_limit)
guessed_number= int(input(f"Guess a number between 1 and {highest_limit}: "))
print(f"Correct number is: {correct_number}")
while guessed_number != correct_number:
	print("Incorrect guess. Try again")
	guessed_number = int(input("Guess a number: "))
	if guessed_number == correct_number:
		print("Correct! You guessed the number")