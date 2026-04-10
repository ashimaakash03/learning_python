#immutable types: int, float, bool

print("Immutability in Boolean")
result= True
another_result= result

print(id(result))
print(id(another_result))
# Both the lines above have the same output

result= False
print(id(result)) #different output because result now points to False object
# which is different from True object
print(id(another_result)) #another_result still points to the True object

print("Immutability in String")
string= "Ashim"
another_string= string
print(id(string))
print(id(another_string))
# Both the lines above have the same output

string += "Aakash"
print(id(string)) #different output because result now points to new value
print(id(another_string)) #another_result still points to "Ashim"

#mutable types: list, set, dict
print("Mutability in Lists")
computer_parts= ["computer",
                 "monitor",
                 "keyboard",
                 "mouse",
                 "mouse pad"]
another_list= computer_parts
print(id(computer_parts))
print(id(another_list))
# Both the lines above have the same output
computer_parts += ["console"] # same as appending at the end of list
print(computer_parts)
print(id(computer_parts)) # same output as two lines above, because lists are
# mutable. No new objects are created
print(another_list)
print(id(another_list))
another_shopping_list= another_list
# 1 list, 3 names: computer_parts, another_list, another_shopping_list
print("All 3 variables point to the same object")
print("computer_parts: {}".format(id(computer_parts)))
print("another_list: {}".format(id(another_list)))
print("another_shopping_list: {}".format(id(another_shopping_list)))