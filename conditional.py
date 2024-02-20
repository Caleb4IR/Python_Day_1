person1 = input("Please give your name ")
height1 = int(input("Please give your height in cm "))
person2 = input("Please give your name ")
height2 = int(input("Please give your height in cm "))

#if (height1 > height2):
#  print(f"{person1} is taller than {person2}")
#else:
#  print(f"{person2} is taller than {person1}")


if (height1 > height2):
  print(f"{person1} is taller than {person2}")
elif (height1 == height2):
  print(f"{person1} and {person2} are the same height")
else:
  print(f"{person2} is taller than {person1}")