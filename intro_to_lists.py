computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse pad"]  # lists are created using sq brackets []

# print a list
for part in computer_parts:
	print(part)  # This will print each individual list item in new line
print(computer_parts)  # This will print all elements in the form of a list
print()
print(computer_parts[2])  # Output: keyboard
print(
	computer_parts[0:3])  # Output: [computer, monitor, keyboard] (index 0
# to 2)
print(computer_parts[-1])  # Output: mouse pad (index -1 to access last element)
