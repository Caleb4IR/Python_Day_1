# try:
#     result = 10 / 0
#     print("The answer is", result)

# except ZeroDivisionError:
#     # When error happens
#     print("Can't divide by 0")
# else:
#     # When no error
#     print("Division was successful")
# finally:
#     # Runs no matter what, whether there is or isn't an error
#     print("operation done")

# print("Hiii")


# def math_divide(n1, n2):
#     try:
#         result = n1 / n2
#         print("The answer is", result)

#     except ZeroDivisionError:
#         # When error happens
#         print("Can't divide by 0")
#     else:
#         # When no error
#         print("Division was successful")
#     finally:
#         # Runs no matter what, whether there is or isn't an error
#         print("operation done")

# if __name__ == "__main__":
#     math_divide(10, 5)
#     math_divide(20, 0)
#     math_divide("and", 1)

# def calculate_age():
#     age = input("Please tell me your year of birth")

# Task1 and 2->
# Please tell me your birth 2000
# Your age is 24
# ValueError
from datetime import datetime


# def calculate_age():
#     try:
#         date = datetime.now().year
#         year = input("Please tell me your year of birth :")
#         calc_age = date - int(year)
#         return f"Age calculated to be :{calc_age}"
#     except ValueError:
#         print("Invalid input. Please enter a valid year of birth.")


# print(calculate_age())

# if __name__ == "__main__":
#     calculate_age()


# Task 3
# Logical errors
# def calculate_age():
#     try:
#         date = datetime.now().year
#         year = input("Please tell me your year of birth :")

#         if year <= 0:
#             # Raise -> stops further execution
#             # Handling logical errors0

#             raise ValueError("Year cannot be negative")
#         if year > date:
#             raise ValueError("You not Flash from the future")

#         #Code is shield
#         calc_age = date - int(year)
#         return f"Age calculated to be :{calc_age}"
#     except ValueError as err:
#         print("Invalid number", err)


# Create your own Error Class
class NegativeNumberError(Exception):

    def __init__(self, value):
        self.value = value
        self.message = "Negative numbers are not allowed"
        super().__init__(self.message)

    def __str__(self):
        return f"{self.value} -> {self.message}"


def only_positive_num():
    try:
        x = -10
        if x < 0:
            raise NegativeNumberError(x)

    # Match what type of error it is
    except NegativeNumberError as e:  # Assign e to the instance we creating
        print(e)


if __name__ == "__main__":
    only_positive_num()
