#Write a program to continue displaying menu options unless the user quits or
# selects an invalid input

print("Please choose one of the following options:")

print("1. Learn Python")
print("2. Go to the movies")
print("3. Listen to a Podcast")
print("4. Build your application")
print("5. Grab a quick bite")
print("0. Quit")

option= int(input())

while option in [0, 1, 2, 3, 4, 5]:
	if option == 1:
		print(f"You selected option {option}. Welcome to Python tutorials")
		print("What's next on your list?")
		option = int(input())
	elif option == 2:
		print(f"You selected option {option}. Welcome to the movies")
		print("What's next on your list?")
		option = int(input())
	elif option == 3:
		print(f"You selected option {option}. Welcome to the podcasts")
		print("What's next on your list?")
		option = int(input())
	elif option == 4:
		print(f"You selected option {option}. Let's get started")
		print("What's next on your list?")
		option = int(input())
	elif option == 5:
		print(f"You selected option {option}. Let's eat. I am famished")
		print("What's next on your list?")
		option = int(input())
	else:
		print(f"You selected option {option}. That means you quit")
		break
else:
	print("You selected invalid option. Game terminated.")