from datetime import datetime

# recipe = {
#   "name": "Spaghetti Carbonara",
#   "servings": 4,
#   "ingredients": ["200g spaghetti", "100g pancetta", "2 eggs", "1/2 cup grated Parmesan", "1 clove garlic"]
# }


# # Task 1
# # ======= Spaghetti Carbonara =======
# # - 200g spaghetti
# # - 100g pancetta
# # - 2 eggs
# # - 1/2 cup grated Parmesan
# # - 1 clove garlic
# # Serves: 4 people

# # recipe_name = f"{recipe['name']}"
# # print(f"{recipe_name:=^33}:")
# # #print(f"{recipe['name']: =^10}")
# # for ingredient in recipe['ingredients']:
# #     print(f"- {ingredient}")
# # print(f"Serves: {recipe['servings']} people")


# # Task 2
guests = ["Alice", "Bob", "Charlie"]
party_date = datetime(2024, 3, 14)

# # Task 2 - Party Invite
# # *       Alice       *
# # You are invited to the party on March 14, 2024!
# # *        Bob        *
# # You are invited to the party on March 14, 2024!
# # *      Charlie      *
# # You are invited to the party on March 14, 2024!

print("Party Invite")
for guest in guests:
    print(f" *{guest:^10}*")
    print(f" You are invited to the party on {party_date.strftime('%B %d, %Y')}!")


