# Caleb Potts
# 03/03/2024

# Setup Code
# Expected Task: Define a `PotionError` exception and use it in a potion-making function.


class PotionError(Exception):
    pass


def make_potion(ingredients):
    if "unicorn horn" not in ingredients:
        raise PotionError(
            f"{ingredients} is not a valid ingredient for the Love Potion."
        )
    else:
        print("Potion successfully made!")


try:
    ingredients = "Eye of Newt"
    make_potion(ingredients)
except PotionError as e:
    print(f"Error: {e}")
