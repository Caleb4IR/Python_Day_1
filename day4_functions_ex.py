library_list = [
    {"title": "Python Programming", "author": "Eric Matthes", "year": 2019, "available": True},
    {"title": "Automate the Boring Stuff with Python", "author": "Al Sweigart", "year": 2020, "available": True},
    {"title": "Learning Python I", "author": "Mark Lutz", "year": 2013, "available": False},
    {"title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015, "available": True},
    {"title": "Adavance Python", "author": "Mark Lutz", "year": 2015, "available": False},
]

# Task 1
# Add Book Function: Write a function add_book(library, new_book) that adds a new book to the library.
# add_book library new_book

# new_book = {"title": "Learning Python III", "author": "Mark Lutz", "year": 2017, "available": False}

# def add_book(library, new_book):
#   library.append(new_book)

# #Pass by reference
# add_book(library_list, new_book)
# print(library_list)


# Task 2 
# Search Books by Author Function: Write a function search_by_author(library, author_name) that returns a list of books by a specific author.

# result = [   
#   {"title": "Learning Python I", "author": "Mark Lutz", "year": 2013, "available": False},  
#   {"title": "Adavance Python", "author": "Mark Lutz", "year": 2015, "available": False}
# ]

# def search_by_author(library, author_name):
#   result = []
#   for book in library:
#       if book["author"] == author_name:
#           result.append(book)
#   return result

# author_name = input("Enter the name of the author to search for: ")

# result = search_by_author(library_list, author_name)

# print(f"Books by author '{author_name}':")
# print(result)

#Or
# author_name = input("Enter the name of the author to search for: ")

# def search_by_author(library, author_name):
#   result = [book for book in library if book["author"] == author_name]
#   return result
  
# search_by_author(library_list, author_name)

#Task 3
#Check Out Book function: write a function check_out_book(library, title) that marks a book as not available if it exists and is availble in the library

title_given = input("Enter the title of the book to check out: ")

def check_out_book(library, title):
  for book in library:
      if book["title"] == title:
          if book["available"]:
              book["available"] = False
              print(f"The book '{title}' has been checked out.")
          else:
              print(f"The book '{title}' is not available for check out.")
          return
  print(f"The book '{title}' was not found in the library.")

# Call the function to check out a book
check_out_book(library_list, title_given)

# Display the updated library list
print("Updated library list:")
print(library_list)


#Dictionary - Not a sequence but it's an iterable

#One line functions
add = lambda a, b: a + b
print(add(10, 20))

