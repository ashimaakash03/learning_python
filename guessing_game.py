#Guess the number algorithm using binary search approach


low= 1
high= 1000

guesses=0
print(f"Please guess a number between {low} and {high}")
input("Press enter to continue...")

while low<=high:
	guesses+=1
	mid= (low+high)//2
	print(f"Is your number {mid}")
	response= input().strip().upper()

	if response== 'Y':
		print(f"You got it in {guesses} guesses! The number is {mid}")
		break
	elif response== 'H':
		low= mid+1
		print("Searching upper half...")
	elif response== 'L':
		high= mid-1
		print("Searching lower half...")
	else:
		print("You choose to quit the game")
		break