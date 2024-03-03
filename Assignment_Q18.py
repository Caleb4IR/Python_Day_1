# Caleb Potts
# 03/03/2024

# Setup Code
ingredients = ["Moonstone", "Silver Dust", "Dragon Blood"]
# Expected Task: For each pair of ingredients, print out the unique potion they produce.

for i in range(len(ingredients)):
    for j in range(i + 1, len(ingredients)):
        ingredient1 = ingredients[i]
        ingredient2 = ingredients[j]

        if {"Moonstone", "Silver Dust"} == {ingredient1, ingredient2}:
            print("Combining Moonstone and Silver Dust produces a Visibility Potion.")
        elif {"Moonstone", "Dragon Blood"} == {ingredient1, ingredient2}:
            print("Combining Moonstone and Dragon Blood produces a Strength Potion.")
        elif {"Silver Dust", "Dragon Blood"} == {ingredient1, ingredient2}:
            print("Combining Silver Dust and Dragon Blood produces a Fireproof Potion.")
        else:
            print(
                f"Combining {ingredient1} and {ingredient2} produces an Unknown Potion."
            )
