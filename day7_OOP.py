#Object Orientated Programming



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



#Bank Account
#1. acc_no
#2. name
#3. balance

# class Bank:
#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         self.balance = balance

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

#Task 3
#caleb.withdraw(2000) -> Your balance is: R98,000
#caleb.display_balance() -> Your balance is: R98,000

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

#Task 4
#dhara.deposit(10_000) -> succcess. Your balance is: R60,001

# class Bank:
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


# gemma = Bank(123, "Gemma Porril", 15_000)
# dhara = Bank(124, "Dhara Kara", 50_001)
# caleb = Bank(125, "Caleb Potts", 100_000)

# deposited = dhara.deposit(10_000)
# print(deposited)


# Assignment - Bank account statement
# List of dictionaries
# #  id   Date       Type     Amount  
# 1.  1  29 Feb   withdraw       2000
# 2.  2  1 Mar    deposit        6000
# 3.  3  3 Mar    deposit        7000   

class BankStatement:
    def __init__(self):
        self.transactions = []
        self.transaction_id = 0

    def add_transaction(self, acc_no, name, transaction_type, amount, date):
        self.transaction_id += 1
        self.transactions.append({"id": self.transaction_id, "date": date, "type": transaction_type, "amount": amount})

    def format_statement(self):
        formatted_statement = "# {:<5} {:<10} {:<10} {:<10}\n".format("id", "Date", "Type", "Amount")
        for transaction in self.transactions:
            formatted_statement += "{:<2}. {:<5} {:<10} {:<10} R{:<10}\n".format(transaction["id"], transaction["date"], transaction["type"], transaction["amount"])
        return formatted_statement

class Bank:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
    
    def display_balance(self):
        return f"Your balance is: R{self.balance:,.2f}"
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal successful. Your balance is now: R{self.balance:,.2f}"
        else:
            return "Withdrawal failed. Insufficient funds."
        
    def deposit(self, dep_amount):
        if dep_amount > 0:
            self.balance += dep_amount
            return f"Deposit successful. Your balance is now: R{self.balance:,.2f}"
        else:
            return "Deposit failed. Invalid amount."

# Creating Bank instances
gemma = Bank(123, "Gemma Porril", 15_000)
dhara = Bank(124, "Dhara Kara", 50_001)
caleb = Bank(125, "Caleb Potts", 100_000)

# Creating BankStatement instance
bank_statement = BankStatement()

# Recording transactions
gemma.withdraw(2000)
bank_statement.add_transaction(gemma.acc_no, gemma.name, "Withdrawal", 2000, "29 Feb")

dhara.deposit(6000)
bank_statement.add_transaction(dhara.acc_no, dhara.name, "Deposit", 6000, "1 Mar")

dhara.deposit(7000)
bank_statement.add_transaction(dhara.acc_no, dhara.name, "Deposit", 7000, "3 Mar")

# Getting and printing the formatted bank statement
print(bank_statement.format_statement())