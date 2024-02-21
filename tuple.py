#Tuple vs List

#Tuple - Immutable | List mutable
person = ("Alex","SA",20)
print(person, type(person))
print(person.count(20)) # Finds the occurances
print(person.index("SA")) # Gets the index of the value
# index - error if nt found | find - gives -1 if not found