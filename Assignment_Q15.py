# Caleb Potts
# 03/03/2024

# Setup Code
artifacts = [
    {"name": "Cloak of Invisibility", "age": 657, "power": 9.5},
    {"name": "Elder Wand", "age": 1000, "power": 10},
    {"name": "Resurrection Stone", "age": 800, "power": 7},
]
# Expected Task: Sort the artifacts first by age, then by power, using a lambda function.

sorted_artifacts = sorted(artifacts, key=lambda x: (x["age"], x["power"]))

for artifact in sorted_artifacts:
    print(artifact)
