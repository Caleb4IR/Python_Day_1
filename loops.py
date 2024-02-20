# i = 0
# while i < 3:
#   print(i)
#   i += 1

#F2 to rename -> rename symbol
#ctrl + d -> multiple cursor

# maximum = int(input("Enter number of rows: "))

# i = 0

# while i < maximum+1:
#   print(i*"😎")
#   i += 1 

#Or

# no_of_row = int(input("Enter number of rows: "))
# i = 1
# while i <= no_of_row:
#   print("😎" * i)
#   i += 1


# for i in range(3):
#   print(i)

# for i in range(1, 3):
#   print(i)

# for i in range(1, 50, 5):
#   print(i)

# no_of_row = int(input("Enter number of rows: "))

# for i in range(1,no_of_row+1):
#   print('😎'*i)


#Task
player_stats = [10, 30, 60]
# output = []
# for i in range(len(player_stats)):
#   doubled_stats = player_stats[i] * 2
#   output.append(doubled_stats)
# print(output)

#Or

# power_up_stats = []
# for i in range(len(player_stats)):
#   power_up_stats.append(player_stats[i] * 2)
  
# print(power_up_stats)

# #Or
# for i in player_stats:
#   print(i*2)

#List comprehension
#double all my stat fror each stat present in player_stats
# powered_up_stats = [i*2 for i in player_stats]
# print(powered_up_stats)


Avengers = [
    "Hulk",
    "Iron man",
    "Black widow",
    "Captain america",
    "Spider man",
    "Thor",
]

word_lengths = []
#Output should be [4,8,11,15,10,4]

for name in Avengers:
    # Calculate the length of each name and append it to the word_lengths list
    word_lengths.append(len(name))

print(word_lengths)

