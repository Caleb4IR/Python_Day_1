# Caleb Potts
# 02/03/2024

# Setup Code
sales = [
    {"salesperson": "Alice", "amount": 200},
    {"salesperson": "Bob", "amount": 150},
    {"salesperson": "Alice", "amount": 100},
]
# Expected Task: Group sales by salesperson and calculate the total sales amount for each.

sales_totals = {}

for sale in sales:
    salesperson = sale["salesperson"]
    amount = sale["amount"]
    if salesperson in sales_totals:
        sales_totals[salesperson] += amount
    else:
        sales_totals[salesperson] = amount

for salesperson, total in sales_totals.items():
    print(f"{salesperson}: {total}")
