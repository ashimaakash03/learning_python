iterable= "ASHIM AAKASH ROY"

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
		print(f"The square of odd number {num} is {num**2}")
