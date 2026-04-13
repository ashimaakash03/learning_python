# Write a program to append an item to the list according to the user input.

available_items= ["computer", "monitor", "keyboard", "mouse", "mouse pad"]
list_items = []

choice = int(input("Please select the items to add to the list..."))

while choice != 0:
	if choice == 1:
		print(f"You selected option {choice}. Adding computer")
		list_items.append("computer")
		choice = int(input("What do you wish to add next?"))
	elif choice == 2:
		print(f"You selected option {choice}. Adding monitor")
		list_items.append("monitor")
		choice = int(input("What do you wish to add next?"))
	elif choice == 3:
		print(f"You selected option {choice}. Adding keyboard")
		list_items.append("keyboard")
		choice = int(input("What do you wish to add next?"))
	elif choice == 4:
		print(f"You selected option {choice}. Adding mouse")
		list_items.append("mouse")
		choice = int(input("What do you wish to add next?"))
	elif choice == 5:
		print(f"You selected option {choice}. Adding mouse pad")
		list_items.append("mouse pad")
		choice = int(input("What do you wish to add next?"))
	else:
		print("You selected an invalid option. Please select an option "
		      "between 1 to 5")
		for part in available_items:
			print(f"{available_items.index(part)+1}. {part}")
		choice = int(input("What do you wish to add next?"))

else:
	print(f"You selected option {choice}. That means you quit")
	print(f"The list contains: {list_items}")
