# Caleb Potts
# 03/03/2024

# Setup Code
tasks = [
    {"id": 1, "priority": "High", "completed": False},
    {"id": 2, "priority": "Low", "completed": True},
    {"id": 3, "priority": "Medium", "completed": False},
]
# Expected Task: Sort the tasks by "completed" status (False first) and then by priority ("High", "Medium", "Low").

from pprint import pprint


def custom_sort(task):
    return (task["completed"], {"High": 0, "Medium": 1, "Low": 2}[task["priority"]])


sorted_tasks = sorted(tasks, key=custom_sort)

pprint(sorted_tasks)
