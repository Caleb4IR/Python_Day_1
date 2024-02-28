# Object Orientated Programming


# ferrari = Car()
# ferrari.name = "Ferrari"
# ferrari.engine = "V8"
# ferrari.wheels = 4
# ferrari.doors = 2

# toyota = Car()
# toyota.name = "Ferrari"
# toyota.engine = "V8"
# toyota.wheels = 4
# toyota.doors = 2

# print(ferrari.name, ferrari.wheels)

# Car -> Blueprint | Class blueprint object
# class Car:
#     def __init__(self, name, engine, wheels, doors):

#         self.name = name
#         self.engine = engine
#         self.wheels = wheels
#         self.doors = doors


#     def horn(self):
#         return "Vroom Vroom"

# # self -> to the object created
# # ferrari -> object
# # __init__ -> first method called

# ferrari = Car("Ferrari", "V8", 4, 2)
# toyota = Car("Toyota", "V4", 4, 4)
# rezvani = Car("Rezvani", "V8", 4, 4)
# porshe = Car("Porshe 911 GT3 RS", "V6", 4, 2)

# print(ferrari.name, ferrari.wheels)
# print(ferrari.horn())
# print(toyota.name, toyota.wheels)
# print(rezvani.name, rezvani.engine, rezvani.wheels)
# print(porshe.name, porshe.engine, porshe.wheels)


# Bank Account
# 1. acc_no
# 2. name
# 3. balance

# class Bank:
#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         self.balance = balance

# gemma, dhara, caleb - objects/instances of bank
# gemma = Bank(123, "Gemma Porril", 15000)
# dhara = Bank(124, "Dhara Kara", 50001)
# caleb = Bank(125, "Caleb Potts", 100000)

# #Task 2
# #gemma.display_balance() -> Your balance is: R15,000

# class Bank:
#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         self.balance = balance

#     def display_balance(self):
#         return f"Your balance is: R{self.balance:,}"

# gemma = Bank(123, "Gemma Porril", 15_000)
# dhara = Bank(124, "Dhara Kara", 50_001)
# caleb = Bank(125, "Caleb Potts", 100_000)

# print(gemma.display_balance())

# Task 3
# caleb.withdraw(2000) -> Your balance is: R98,000
# caleb.display_balance() -> Your balance is: R98,000

# class Bank:
#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         self.balance = balance

#     def display_balance(self):
#         print(f"Your balance is: R{self.balance:,.2f}")

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrawal successful. Your balance is now: R{self.balance:,.2f}")
#         else:
#             print("Withdrawal failed. Insufficient funds.")

# gemma = Bank(123, "Gemma Porril", 15_000)
# dhara = Bank(124, "Dhara Kara", 50001)
# caleb = Bank(125, "Caleb Potts", 100000)

# caleb.withdraw(2000)
# caleb.display_balance()

# # Task 4
# # dhara.deposit(10_000) -> succcess. Your balance is: R60,001

# class Bank1:
#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         self.balance = balance

#     def display_balance(self):
#         return f"Your balance is: R{self.balance:,.2f}"

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             return f"Withdrawal successful. Your balance is now: R{self.balance:,.2f}"
#         else:
#             return "Withdrawal failed. Insufficient funds."

#     def deposit(self, dep_amount):
#         if dep_amount > 0:
#             self.balance += dep_amount
#             return f"Deposit successful. Your balance is now: R{self.balance:,.2f}"
#         else:
#             return "Deposit failed. Invalid amount."


# gemma = Bank1(123, "Gemma Porril", 15_000)
# dhara = Bank1(124, "Dhara Kara", 50_001)
# caleb = Bank1(125, "Caleb Potts", 100_000)

# deposited = dhara.deposit(10_000)
# print(deposited)


# Assignment - Bank account statement
# List of dictionaries
# #  id   Date       Type     Amount
# 1.  1  29 Feb   withdraw       2000
# 2.  2  1 Mar    deposit        6000
# 3.  3  3 Mar    deposit        7000

# class variables


# class Bank:
#     interest_rate = 0.02

#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         self.balance = balance

#         # Task 2
#         # insance method

#     def display_balance(self):
#         return f"Your balance is: R{self.balance:,.2f}"

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             return f"Withdrawal successful. Your balance is now: R{self.balance:,.2f}"
#         else:
#             return "Withdrawal failed. Insufficient funds."

#     def deposit(self, amount):
#         if dep_amount > 0:
#             self.balance += dep_amount
#             return f"Deposit successful. Your balance is now: R{self.balance:,.2f}"
#         else:
#             return "Deposit failed. Invalid amount."

#     def apply_interest(self):
#         self.balance = self.balance + self.balance * Bank.interest_rate
#         return f"Interest added. Your balance is now: R{self.balance:,.2f}"


# gemma = Bank(123, "Gemma Porril", 15_000)
# dhara = Bank(124, "Dhara Kara", 50_001)
# caleb = Bank(125, "Caleb Potts", 100_000)

# gemma.apply_interest()
# dhara.apply_interest()
# caleb.apply_interest()

# print(gemma.display_balance())
# print(dhara.display_balance())
# print(caleb.display_balance())


# Encapsulation | Putting in all together container | giving access
class Bank2:
    interest_rate = 0.02

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        # Private variable
        self.__balance = balance

        # Task 2
        # insance method

    def display_balance(self):
        return f"Your balance is: R{self.__balance:,.2f}"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrawal successful. Your balance is now: R{self.__balance:,.2f}"
        else:
            return "Withdrawal failed. Insufficient funds."

    def deposit(self, amount):
        if dep_amount > 0:
            self.__balance += dep_amount
            return f"Deposit successful. Your balance is now: R{self.__balance:,.2f}"
        else:
            return "Deposit failed. Invalid amount."

    def apply_interest(self):
        self.__balance = self.__balance + self.__balance * Bank2.interest_rate
        return f"Interest added. Your balance is now: R{self.__balance:,.2f}"


gemma = Bank2(123, "Gemma Porril", 15_000)
dhara = Bank2(124, "Dhara Kara", 50_001)
caleb = Bank2(125, "Caleb Potts", 100_000)

gemma.apply_interest()
dhara.apply_interest()
caleb.apply_interest()

print(gemma.display_balance())
print(dhara.display_balance())
print(caleb.display_balance())

print(gemma.display_balance())
