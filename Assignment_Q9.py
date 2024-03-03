# Caleb Potts
# 02/03/2024

# Setup Code
books = [
    {"title": "A History of Magic", "pages": 100},
    {"title": "Magical Drafts and Potions", "pages": 150},
]
# Expected Task: Filter books with more than 120 pages and format their titles to uppercase.

filtered_books = [book["title"].upper() for book in books if book["pages"] > 120]

print(filtered_books)
