# Caleb Potts
# 03/03/2024

# Setup Code
adopters = [("Harry", "Phoenix"), ("Hermione", "House Elf")]
creatures = [("Fawkes", "Phoenix"), ("Dobby", "House Elf"), ("Buckbeak", "Hippogriff")]
# Expected Task: Use `filter` and `map` to create a list of matches between adopters and creatures.


matches = filter(
    lambda adopter: any(adopter[1] == creature[1] for creature in creatures), adopters
)
matches_with_names = map(
    lambda match: (
        match[0],
        next(creature[0] for creature in creatures if creature[1] == match[1]),
    ),
    matches,
)

matches_with_names = list(matches_with_names)

print(matches_with_names)
