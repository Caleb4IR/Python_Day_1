#String, List, Tuple, Dictionary, Sets
#Sets - Like list they mutable but only have unique values
#Unordered

# tech_gadgets = {"Smartphone", "Laptop", "Smartwatch", "Tablet"}
# tech_gadgets_list = ["Smartphone", "Laptop", "Smartwatch", "Tablet", "Tablet"]
# print(tech_gadgets)
# print(tech_gadgets_list)

# #Add
# tech_gadgets.add("E-reader")
# print(tech_gadgets)

# #Multiple
# more_gadgets = ["Drone", "Selfiestick"]
# tech_gadgets.update(more_gadgets)
# print(tech_gadgets)

# #Delete
# #.remove -> error if not found | .discard -> no error if not found
# tech_gadgets.discard("Drone")
# print(tech_gadgets)

# #Empty Set
# # x = set()
# # print(type(x))
# # x.add("Caleb")


# outdoor_activities = {"Hiking", "Cycling", "Swimming",}
# indoor_activities = {"Gaming", "Reading", "Cycling"}

# print(indoor_activities.intersection(outdoor_activities))
# print(indoor_activities.union(outdoor_activities))

# print(indoor_activities.difference(outdoor_activities))
# print(outdoor_activities.difference(indoor_activities))

# print(outdoor_activities.symmetric_difference(indoor_activities)) #Opp intersection


# colors = ["red", "blue", "red", "green", "pink", "blue"]
# #Output should be ["red", "blue", "green", "pink"]

# #Task1 - easy way
# colors1 = set(colors)
# print(colors1)

# #Task2- hard way
# # Use methods to remove duplicates
# colors2 = []
# for color in colors:
#   if color not in colors2:
#     colors2.append(color)
# print(colors2)

# #Task2- hard way
# # Use add method to remove duplicates
# colors3 = set()
# for color in colors:
#   colors3.add(color)

# print(list(set(colors3)))



outdoor_activities = {'Hiking', 'Cycling', 'Swimming'}
indoor_activities = {'Gaming', 'Reading', 'Cycling'}
activity_gadgets = {'Smartwatch': 'Hiking', 'VR Headset': 'Gaming', 'Smartphone': 'Reading', 'Drone': 'Cycling'}

# Task 1
# Which are outdoor_gadgets ? 
# {'Smartwatch',  'Drone'}
outdoor_gadgets = set()

for gadget, activity in activity_gadgets.items():
    if activity in outdoor_activities:
        outdoor_gadgets.add(gadget)

print(outdoor_gadgets)


# Task 2
# # Which are indoor_gadgets ?
indoor_gadgets = set()

for gadget, activity in activity_gadgets.items():
    if activity in indoor_activities:
        indoor_gadgets.add(gadget)

print(indoor_gadgets)

#Task 3 - implement DRY
def findGad(activity_gadgets,activities):
  gadgets = set()
  for gadget in activity_gadgets:
    if (activity_gadgets[gadget] in activities):
      gadgets.add(gadget)
  return gadgets

print(findGad(activity_gadgets, outdoor_activities))
print(findGad(activity_gadgets, indoor_activities))


outdoor_gadgets = {gadget for gadget, activity in activity_gadgets.items() if activity in outdoor_activities}
print(outdoor_gadgets)

indoor_gadgets = {gadget for gadget, activity in activity_gadgets.items() if activity in indoor_activities}
print(indoor_gadgets)

#Or

def findGad(activity_gadgets,activities):
  return {gadget for gadget, activity in activity_gadgets.items() if activity in activities}

print(findGad(activity_gadgets, outdoor_activities))
print(findGad(activity_gadgets, indoor_activities))





