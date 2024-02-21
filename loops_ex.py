numbers = [8, 5, 7, 4, 6, 2]

# #["Even", "Odd", "Odd", "Even", "Even", "Even"]
# sorted = []
# for i in numbers:
#   if i % 2 == 0:
#     sorted.append("Even")
#   else:
#     sorted.append("Odd")

# print(sorted)

#Or
sorted = ["Even" if i % 2 == 0 else "Odd" for i in numbers]
print(sorted)