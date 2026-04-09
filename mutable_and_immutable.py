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

print("Immutability in Boolean")
string= "Ashim"
another_string= string
print(id(string))
print(id(another_string))
# Both the lines above have the same output

string += "Aakash"
print(id(string)) #different output because result now points to new value
print(id(another_string)) #another_result still points to "Ashim"