# Caleb Potts
# 03/03/2024

# Setup Code
house_points = [
    {"house": "Gryffindor", "points": 35},
    {"house": "Slytherin", "points": 50},
    {"house": "Gryffindor", "points": 60},
    {"house": "Slytherin", "points": 40},
]
# Expected Task: Aggregate points for each house and print the total.


house_points_aggregated = {}

for entry in house_points:
    house = entry["house"]
    points = entry["points"]
    if house in house_points_aggregated:
        house_points_aggregated[house] += points
    else:
        house_points_aggregated[house] = points

for house, total_points in house_points_aggregated.items():
    print(f"{house}: {total_points} points")
