# Caleb Potts
# 02/03/2024

# Setup Code
orders = [
    {
        "order_id": 1,
        "items": [{"product": "A", "quantity": 2}, {"product": "B", "quantity": 3}],
    },
    {
        "order_id": 2,
        "items": [{"product": "A", "quantity": 1}, {"product": "C", "quantity": 1}],
    },
]
# Expected Task: Transform this list into a dictionary where keys are product names and values are total quantities ordered across all orders.

product_quantities = {}

for order in orders:
    for item in order["items"]:
        product = item["product"]
        quantity = item["quantity"]
        if product in product_quantities:
            product_quantities[product] += quantity
        else:
            product_quantities[product] = quantity

print(product_quantities)
