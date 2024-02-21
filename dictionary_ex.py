# books = [
#   {"title": "Infinite Jest", "rating": 4.5, "genre": "Fiction"},
#   {"title": "A Brief History of Time", "rating": 4.8, "genre": "Science"},
#   {"title": "The Catcher in the Rye", "rating": 3.9, "genre": "Fiction"},
#   {"title": "Sapiens", "rating": 4.9, "genre": "History"},
#   {"title": "Clean Code", "rating": 4.7, "genre": "Technology"},
# ]

# #Get all highly rated books with 4.7 rating and above
# #Expected Output: ["A Brief History of Time", "Clean Code", "Sapiens"]
# highly_rated_books = []
# for book in books:
#  if book["rating"] >= 4.7:
#    highly_rated_books.append(book["title"])
# print(highly_rated_books)


# #Task2 - List Comprehension
# highly_rated_books = [book["title"] for book in books if book["rating"] >= 4.7]
# print(highly_rated_books)

# #Task3
# highly_rated_books = sorted([book["title"] for book in books if book["rating"] >= 4.7])
# print(highly_rated_books)



#Task 1
# inventory = [
#   {"name": "Apple", "quantity": 30, "price": 0.50},
#   {"name": "Banana", "quantity": 20, "price": 0.20}
# ]
# #What is the product name?
# #What is the quantity?
# #What is the price?
# #Add that new product into the list

# # product_name = input("Enter the product name: ")
# # product_quantity = int(input("Enter the quantity: "))
# # product_price = float(input("Enter the price: "))
# # new_product = {"name": product_name, "quantity": product_quantity, "price": product_price}

# # inventory.append(new_product)
# # print(inventory)


# #Clue

# #Task 2
# #If product already exists, then add the quantity to the existing quantity
# #If product already exists, then update the price
# #If product does not exist, then add the product into the list

# product_name = input("Enter the product name: ")
# product_quantity = int(input("Enter the quantity: "))
# product_price = float(input("Enter the price: "))
# new_product = {"name": product_name, "quantity": product_quantity, "price": product_price}

# for product in inventory:
#   if product["name"] == product_name:
#       product_exists = True
#       product["quantity"] += product_quantity  
#       product["price"] = product_price  
  
# print(inventory)

# #Or

# for product_name in inventory:
#   if product_name["name"] == product_name:
#     product["quantity"] += product_quantity  
#     product["price"] = product_price  


# #Taks 3: Not exists then add to the inventory
# # roduct_name = input("Enter the product name: ")
# # product_quantity = int(input("Enter the quantity: "))
# # product_price = float(input("Enter the price: "))
# # new_product = {"name": product_name, "quantity": product_quantity, "price": product_price}

# # product_exists = False
# # for product in inventory:
# #   if product["name"] == product_name:
# #       product_exists = True
# #       product["quantity"] += product_quantity  # Add to existing quantity
# #       product["price"] = product_price  # Update price
# #       break
# # if not product_exists:
# #   new_product = {"name": product_name, "quantity": product_quantity, "price": product_price}
# #   inventory.append(new_product)

# # print(inventory)

# #Or
# product_name = input("Enter the product name: ")
# product_quantity = int(input("Enter the quantity: "))
# product_price = float(input("Enter the price: "))
# new_product = {"name": product_name, "quantity": product_quantity, "price": product_price}

# product_exists = False
# for product in inventory:
#   if product["name"] == product_name:
#       product["quantity"] += product_quantity  
#       product["price"] = product_price
#       break
#   #Only when break not happen to else
# else:
#   inventory.append(new_product)

# print(inventory)



#5 pillars -> Good quality code

#1. Readibility - 70% reading as a developer and 30% coding
#2. Maintaineability - 80% coding and 20% maintaineance
#3. Extendability
#4. Testability
#5. Performance



# guests = [
#   {"name": "Alice", "age": 25, "code": "VIP123"},
#   {"name": "Bob", "age": 17, "code": "VIP123"},
#   {"name": "Charlie", "age": 30, "code": "VIP123"},
#   {"name": "Dave", "age": 22, "code": "GUEST"},
#   {"name": "Eve", "age": 29, "code": "VIP123"}
# ]

# blacklist = ["Dave", "Eve"]


# # Output
# # People who are 21 or above and VIP123
# # Blacklist are not allowed

# # ["Alice", "Charlie"]
# allowed_guest = []
# for guest in guests:
#   if guest["age"] >= 21 and guest["code"] == "VIP123" and guest["name"] not in blacklist:
#     allowed_guest.append(guest["name"])
# print(allowed_guest)

# #OR
# #PEP - Pythone Enhancement Proposal 8

# allowed_guest = []
# PASS_CODE = "VIP123"

# for guest in guests:
#   if guest["age"] >= 21 and guest["code"] == PASS_CODE and guest["name"] not in blacklist:
#     allowed_guest.append(guest["name"])
# print(allowed_guest)

# allowe_guest = [guest["name"] for guest in guests if guest["age"] >= 21 and guest["code"] == PASS_CODE and guest["name"] not in blacklist]


# nums = [90, 50, 80]

# for idx in range(len(nums)):
#   print(idx, nums[idx])

# for num in enumerate(nums):
#   print(num)

# for idx, num in enumerate(nums):
#   print(idx, num)


# employee = [
#   {"name": "alex", "experience": 2},
#   {"name": "Gemma"},
#   {"name": "Rashay", "age": 4},
#   {"name": "Thato"},
# ]

# #2024
# #Expected Output
# #Task 1, Task2 - Use get()
# # [
# #   {"name": "alex", "experience": 3},
# #   {"name": "Gemma", "experience": 1},
# #   {"name": "Rashay", "experience": 5},
# #   {"name": "Thato", "experience": 1},
# # ]



# for employee in employees:
#   employee["experience"] = employee.get("experience", 0) + 1

# print(employees)

# #Task 3
# #senior is 5 or more experience
# #Mid Level is 3-5
# #Junior level is less than 3

# #Expected Output
# # [
# #   {"name": "alex", "experience": 3, "status": "Mid-Level"},
# #   {"name": "Gemma", "experience": 1, "status": "Junior"},
# #   {"name": "Rashay", "experience": 5, "status": "senior"},
# #   {"name": "Thato", "experience": 1, "status": "Junior"},
# # ]

# for employee in employees:
#   employee["experience"] = employee.get("experience", 0) + 1
#   experience = employee["experience"]
#   if experience >= 5:
#       employee["status"] = "Senior"
#   elif 3 <= experience < 5:
#     employee["status"] = "Mid-Level"
#   else:
#     employee["status"] = "Junior"

# print(employees)


#Copy
# movie = {
#   "name": "Mr Bones",
#   "year": 2001
# }

# movie_copy1 = movie.copy()

# #unpacking operator  * -> List | ** -> Dictionary
# movie_copy2 = {**movie} #Copy
# print(movie_copy2)

# movie_copy2 = {**movie, "rating": 10} #Copy and add
# print(movie_copy2)

# movie_copy3 = {**movie, "rating": 10, "year": 2002}
# print(movie_copy3)

# movie_copy4 = {"rating": 10, "year": 2002, **movie}
# print(movie_copy4)

# movie = {
#   "name": "Mr Bones",
#   "year": 2001
# }

# detail = {
#   "actor": "Lean schuster",
#   "director": "Dzithendo"
# }

# movie_details = {**movie, **detail} #Preferred way to add dictionaries together
# print(movie_details)

price = [1000, 1200, 400]
price_copy = [*price] # Copy 

price_copy1 = [50, 40, *price, 60]
print(price_copy, price_copy1)

t1 = [80, 90]
t2 = [50, 60]
t3 = [*t1, *t2]
print(t3)