import json

# data = {
#     "employees": [
#         {"name": "Alice", "age": 30, "department": "Sales"},
#         {"name": "Bob", "age": 25, "department": "Marketing"},
#     ]
# }

# print(type(data))

# print(data["employees"][0]["age"])

# data_json = json.dumps(data, indent=4)
# print(data_json, type(data_json))

# # JSON - JavaScript Object Notation

# sport = {"name": "Dhoni", "dbl": lambda x: x * 2}

# print(sport["dbl"](10))

# sport_json = json.dumps(
#     sport
# )  # JSON serializable(Convert) | Can't convert Dictionary because it contains a function
# # print(sport_json) #Invalid JSON

# student_json = """
#     {
#         "name": "gemma",
#         "gender":"female"
#     }
# """

# # print(student_json["name"]) # error
# student = json.loads(student_json)

# print(student["name"])


# # All active users - increase their balance by 10% - final output should be in JSON format
# bank_data = """
# [
#     {
#         "id": 1,
#         "name": "John Doe",
#         "email": "johndoe@example.com",
#         "isActive": true,
#         "balance": 150.75
#     },
#     {
#         "id": 2,
#         "name": "Jane Smith",
#         "email": "janesmith@example.com",
#         "isActive": false,
#         "balance": 500.50
#     },
#     {
#         "id": 3,
#         "name": "Emily Jones",
#         "email": "emilyjones@example.com",
#         "isActive": true,
#         "balance": 0.00
#     }
# ]
# """
# # Task 1
# bank_accounts = json.loads(bank_data)

# for account in bank_accounts:
#     if account["isActive"]:
#         account["balance"] *= 1.1

# updated_bank_data = json.dumps(bank_accounts, indent=4)

# print(updated_bank_data)

# bank_accounts = json.loads(bank_data)


# # Task 2
# bank_accounts = json.loads(bank_data)

# updated_bank_data = [
#     {**account, "balance": account["balance"] * 1.1} if account["isActive"] else account
#     for account in bank_accounts
# ]
# converted = json.dumps(updated_bank_data, indent=4)

# # print(converted)

# # Write a file
# with open("bank_accounts.json", "w") as file:
#     json.dump(updated_bank_data, file, indent=4)

# # Read a file
# with open("bank_accounts.json", "r") as file:
#     data = json.load(file)
#     print(data)


with open("blog_post.json", "r") as file:
    data = json.load(file)

posts_summary = []
for post in data["posts"]:
    summary_item = {
        "title": post["title"],
        "author": post["author"],
        "number_of_comments": len(post["comments"]),
    }
    posts_summary.append(summary_item)

with open("posts_summary.json", "w") as file:
    json.dump({"posts_summary": posts_summary}, file, indent=4)
