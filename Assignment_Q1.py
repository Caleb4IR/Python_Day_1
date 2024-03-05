# Caleb Potts
# 02/03/2024

# Setup Code
students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 75},
    {"name": "Charlie", "grade": 93},
]
# Expected Task: Sort the list of dictionaries by grade in descending order and add a "rank" key to each dictionary based on the sorting.

# 1st Code
def get_grade(student):
    return student["grade"]

students_sorted = sorted(students, key=get_grade, reverse=True)

for i, student in enumerate(students_sorted):
    student["rank"] = i + 1

for student in students_sorted:
    print(student)

