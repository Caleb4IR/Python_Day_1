# Caleb Potts
# 02/03/2024

# Setup Code
ingredients = ["Wolfsbane", "Eye of Newt", "Dragon Scale"]
# Expected Task: Use `map` to append ": 3 grams" to each ingredient.


def add_units(ingredient):
    return ingredient + ": 3 grams"


ingredients_with_units = map(add_units, ingredients)
print(list(ingredients_with_units))
