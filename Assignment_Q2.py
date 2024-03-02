# Caleb Potts
# 02/03/2024

# Setup Code
employees = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
salaries = [{"id": 1, "salary": 50000}, {"id": 2, "salary": 60000}]
# Expected Task: Merge these lists into a single list of dictionaries by matching the "id" field, including all keys.


# 1st Code
salary_dict = {}
for salary in salaries:
    salary_dict[salary["id"]] = salary["salary"]

merged_list = []
for employee in employees:
    employee_id = employee["id"]
    if employee_id in salary_dict:
        merged_dict = employee.copy()
        merged_dict["salary"] = salary_dict[employee_id]
        merged_list.append(merged_dict)

for item in merged_list:
    print(item)


# Improved
salary_dict = {salary["id"]: salary["salary"] for salary in salaries}

merged_list = []
for employee in employees:
    employee_id = employee["id"]
    if employee_id in salary_dict:
        merged_dict = {**employee, "salary": salary_dict[employee_id]}
        merged_list.append(merged_dict)

for item in merged_list:
    print(item)
