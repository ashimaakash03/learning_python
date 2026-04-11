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

# min and max
numbers = [12, 34, 56, 78, 90, 23, 45, 67, 89]
print(f"Minimum in the list: {min(numbers)}")
print(f"Maximum in the list: {max(numbers)}")
print(f"Number of elements in the list: {len(numbers)}")

# count function
river = "mississippi"
print(f"Number of 's': {river.count('s')}")  # 4 's' present in mississippi
print(f"Number of 'i': {river.count('i')}")  # 4 'i' present in mississippi
print(
	f"Number of 'iss': {river.count('iss')}")  # 2 'iss' present in mississippi
