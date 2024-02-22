# Dictionary -> Hashmap -> Key: Value
# Key: Unique | Value: Duplicate

# person = {
#   "name": "Siya Kolisi",
#   "age": 32,
#   "country": "South Africa",
#   "sport": "Rugby"
# }

# print(person, type(person))
# print(person["name"])
# person["age"] += 1
# print(person)

# #Methods
# #Iterable -> List, Tuple, dict_keys
# print(person.keys())
# print(person.values())
# print(person.items())

# #loop
# person = {
#   "name": "Siya Kolisi",
#   "age": 32,
#   "country": "South Africa",
#   "sport": "Rugby"
# }

# for detail in person.items():
#   print(detail[0])

# for key, value in person.items():
#   print(key,value)

# print(person["height"]) # Error
# #safety for value when using "get()"
# print(person.get("height")) #None
# #get("key", default value)
# print(person.get("height", 175))


person = {
  "name": "Siya Kolisi",
  "age": 32,
  "address": {
    "city": "Port Elizabeth",
    "country": "South Africa"
  },
  "school" : "Grey high school",
  "height": 186,
  "sport": "Rugby"
}
print(person["address"]["city"])
#AttributeError: 'NoneType' object has no attribute 'get'
#print(person.get("stats").get("points"))

print(person.get("stats", {}))

print(person.get("stats", {}).get("points"))

print(person.get("stats", {}).get("points", "No values"))


#Dictionary comprehension
nums = {x: x for x in range(10)}
nums = {x: x**2 for x in range(10)}
nums = {x: x**2 for x in range(10) if x % 2 == 0}

