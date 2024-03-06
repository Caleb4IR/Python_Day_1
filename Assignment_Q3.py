# Caleb Potts
# 02/03/2024

# Setup Code
products = [
    {"id": 1, "category": "Electronics", "price": 850},
    {"id": 2, "category": "Furniture", "price": 1200},
    {"id": 3, "category": "Electronics", "price": 400},
]
# Expected Task: Filter the list to include only products in the "Electronics" category with a price less than 500.

filtered_products = [
    product
    for product in products
    if product["category"] == "Electronics" and product["price"] < 500
]

for product in filtered_products:
    print(product)