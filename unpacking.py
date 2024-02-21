# a = 10
# b = 10
# c = 10
#Multiple variable assignment
# a = b = c = 10
# print(a,b,c)

# lilitha, Dhara, Quinlan = "Chocolate", "Lime", "Vanilla"
# print(lilitha, Dhara, Quinlan)

# movies = ["Remember the Titans", "Juno", "Lucy"]
# caleb, gemma, yolanda =  ["Remember the Titans", "Juno", "Lucy"]
# print(gemma)

# t1, t2, t3 = [100, 200, 300, 400] # Error
# print(t1, t2, t3) 

# t1, t2, t3, _ = [100, 200, 300, 400] # "_" is the wildcard sharacter
# print(t1, t2, t3) # _ -> skip

# t1, _, t2, t3 = [100, 200, 300, 400, 60, 40, 30] # "_" is the wildcard sharacter
# print(t1, t2, t3) # _ -> skip

# t1, t2, *t3 = [100, 200, 300, 400, 60, 40, 30] # "*" unpacking operator
# print(t1, t2, t3) # t3 will be a list

# t1, t2, *t3 = (100, 200, 300, 400, 60, 40, 30) # "*" unpacking operator
# print(t1, t2, t3) # t3 will be a list


# coordinate = [(5, 4), (1, 1), (6, 10), (9,10)] # coordinates list of tuple
# # from Rrigin (0, 0)

#Task 1
import math

# coordinates = [(5, 4), (1, 1), (6, 10), (9, 10)]

# distances = []

# for x, y in coordinates:
#     distance = math.sqrt(x**2 + y**2)
#     distances.append(distance)

# print(distances)

#Or


#Task 2 - use unpacking
coordinates = [(5, 4), (1, 1), (6, 10), (9, 10)]

distances = []

for x, y in coordinates:
    distance = math.sqrt(x**2 + y**2)
    distances.append(distance)

print(distances)


#Task 3 - use unpacking and unpacking

coordinates = [(5, 4), (1, 1), (6, 10), (9, 10)]

distances = [math.sqrt(x**2 + y**2) for x, y in coordinates]
print(distances)