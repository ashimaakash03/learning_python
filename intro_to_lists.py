computer_parts= ["computer",
                 "monitor",
                 "keyboard",
                 "mouse",
                 "mouse pad"] #lists are created using sq brackets []

#print a list
for part in computer_parts:
	print(part)
print()
print(computer_parts[2]) # Output: keyboard
print(computer_parts[0:3]) #Output: [computer, monitor, keyboard] (index 0 to 2)
print(computer_parts[-1]) # Output: mouse pad (index -1 to access last element)