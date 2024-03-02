# Caleb Potts
# 02/03/2024

# Setup Code
spells = [("Lumos", 5), ("Obliviate", 10), ("Expelliarmus", 7)]
# Expected Task: Sort the spells list by power level in descending order using a lambda function.

sorted_spells = sorted(spells, key=lambda x: x[1], reverse=True)

for spell in sorted_spells:
    print(spell)
