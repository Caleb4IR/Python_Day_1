#lime
#Yes, we do have it

#Strawberry
#No, we ran out of stock

#Task 1
# stock1 = "vanilla"
# stock2 = "lime"
# stock3 = "chocolate"

# flavour1 = input("What flavour would you like? ")
# if (flavour1 in stock1 or flavour1 in stock2 or flavour1 in stock3):
#  print(f"Yes, we do have {flavour1}")
# else:
#  print(f"No, we ran out of stock")


#Task 2
shop_stock = "vanilla, lime, chocolate"

#in operator | Membership operator | boolean
# Refactor --> Code Quality (up)

flavour = input("What flavour would you like? ")
# if (flavour in shop_stock):
#  print(f"Yes, we do have {flavour}")
# else:
#  print(f"No, we ran out of stock")


#Tertiary operator(3 operands)
#Condition ___if condition else ___
message = "Yes we do have " + flavour if flavour in shop_stock else "No we ran out of stock"
print(message)


#Binary Operator(2 operands)
#>,<, ==, >=, <=
# and, or
# = asigment operator

#Unary Operator(1 operand)
#not
# ~(no practical use)

  
#1 -> 1
#2 -> 10
#3 -> 11
#4 -> 100


  