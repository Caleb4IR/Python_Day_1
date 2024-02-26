from pprint import pprint
classes = {

    "Class A": [
        {"name": "Alice", "grades": [82, 90, 88]},
        {"name": "Bob", "grades": [78, 81, 86]},
        {"name": "Charlie", "grades": [85, 85, 87]}
    ],

    "Class B": [
        {"name": "Dave", "grades": [92, 93, 88]},
        {"name": "Eve", "grades": [76, 88, 91]},
        {"name": "Frank", "grades": [88, 90, 92]}
    ]

}

#Find the average of each class
#Task 1
#Output = {"Class A": 85.0, "Class B": 87.0}

class_averages = {}

for class_name, students in classes.items():
    total_avg = 0
    for student in students:
        avg_grade = sum(student["grades"]) / len(student["grades"])
        total_avg += avg_grade
    class_avg = round(total_avg / len(students),2)
    class_averages[class_name] = class_avg

print(class_averages)


#Task2
#Assume student names are unique
#Student average
#Output = {"Class A": {"Alice": 85.0, "Bob": 87.0, "Charlie": 85.0},
#          "Class B": {"Dave": 87.0, "Eve": 88.0, "Frank": 90"}

student_averages = {}

for class_name, students in classes.items():
    student_averages[class_name] = {}
    for student in students:
        avg_grade = round(sum(student["grades"]) / len(student["grades"]),2)
        student_averages[class_name][student["name"]] = avg_grade

pprint(student_averages)

#Task 3: Task1 + list comprehension
class_averages = {
  class_name: round(sum(sum(student["grades"]) / len(student["grades"]) for student in students) / len(students),2)
  for class_name, students in classes.items()
}

pprint(class_averages)


#Task 4: Taskk2 + list comprehension
# student_averages = {
#   class_name: {student["name"]: round(sum(student["grades"]) / len(student["grades"]),2) for student in students}
#   for class_name, students in classes.items()
# }

# pprint(student_averages)

def find_avg(nums):
  return round(sum(nums) / len(nums), 2)

students_avg_dict = {
    cls_name: {student['name']: find_avg(student['grades']) for student in students}
    for cls_name, students in classes.items()
}
