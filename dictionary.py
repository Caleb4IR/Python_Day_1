# Dictionary -> Hashmap -> Key: Value
# Key: Unique | Value: Duplicate

person = {
  "name": "Siya Kolisi",
  "age": 32,
  "country": "South Africa",
  "sport": "Rugby"
}

print(person, type(person))
print(person["name"])
person["age"] += 1
print(person)

#Methods
#Iterable -> List, Tuple, dict_keys
print(person.keys())
print(person.values())
print(person.items())

#loop
person = {
  "name": "Siya Kolisi",
  "age": 32,
  "country": "South Africa",
  "sport": "Rugby"
}

for detail in person.items():
  print(detail[0])

for key, value in person.items():
  print(key,value)