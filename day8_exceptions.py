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


def math_divide(n1, n2):
    try:
        result = n1 / n2
        print("The answer is", result)

    except ZeroDivisionError:
        # When error happens
        print("Can't divide by 0")
    else:
        # When no error
        print("Division was successful")
    finally:
        # Runs no matter what, whether there is or isn't an error
        print("operation done")


math_divide(10, 5)
math_divide(20, 0)
