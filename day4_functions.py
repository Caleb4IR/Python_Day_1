a = 8
b = 10


a1 = 60
b1 = 70


a2 = 600
b2 = 70



# Functions are ways to pack your logic

# Declaration/Definition
def sum(a,b): #function name #parameters/arguments
  return a + b #body

# Calling/Invoking
print(sum(30, 50))

#Abstraction - you don't need to know how it works to use it } hidig implementation


#default values
# def driving_test(age):
#   if age >= 18:
#     return "You are eligible for driving"
#   else:
#     return "Try again in a few years 👶🏼🍼"

# print(driving_test(20))

def driving_test(name, age, car="Toyota tazz"):
  if age >= 18:
    return f"You {name} are eligible for driving. You will be tested with {car}"
  else:
    return "Try again in a few years 👶🏼🍼"

print(driving_test("Caleb", 20, "GR Corolla"))
print(driving_test("Gemma", 20))

#Types of argument
#Positional argument
#Keyword argument
  #Also used with sort(reverse)

print(driving_test(age=21, name="Alex"))

