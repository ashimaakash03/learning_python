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

#print all numbers from 1 to 20
#here we omitted the start value. Starts from 0 by default
for num in range(21):
	print(f"Number is now {num}")

#Introducing the positive step value. If the step value is omitted, it is considered to be 1
for num in range(0,21, 2):
	print(f"Number is now {num}") # Output is 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20.
#Since step value is 2
for num in range(0,21, 5):
	print(f"Number is now {num}")
# Output is 0, 5, 10, 15, 20. Since step value is 5