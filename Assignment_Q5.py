# Caleb Potts
# 02/03/2024

# Setup Code
transactions = [
    {"date": "2021-01-01", "amount": 100, "category": "Food"},
    {"date": "2021-01-01", "amount": 200, "category": "Transport"},
    {"date": "2021-01-02", "amount": 150, "category": "Food"},
]
# Expected Task: Summarize the total amount spent per category.

category_totals = {}

for transaction in transactions:
    category = transaction["category"]
    amount = transaction["amount"]
    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount

for category, total in category_totals.items():
    print(f"{category}: {total}")
