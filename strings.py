
parrot= "Norwegian Blue"
#positive indexing starts from 0. Maximum is 1 less than size of string
print("Positive")
print(parrot[3].upper())
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
print()
#negative indexing starts from -1. Maximum is negative of size of string
print("Negative")
print(parrot[-11].upper())
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
print("size")
print(len(parrot))
print()
#slicing a string
print(parrot[1:6]) #Starting from index 1, 6 characters 'orweg'
print(parrot[3:5]) #from character at index 3 to character at index 5, not including the character
# at index 5 'we'
print(parrot[0:9]) #from character at index 0 to character at index 9, not including the character
# at index 9 'Norwegian'
print(parrot[:9]) #if we do not provide start index, default is considered as 0.
print(parrot[10:14]) #'Blue'
print(parrot[10:]) #if we do not provide any value after ':', it continues till the end
print(parrot[:9]+parrot[9:]) #whole string is obtained