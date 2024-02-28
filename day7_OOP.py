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
# class Bank2:
#     interest_rate = 0.02

#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         # Private variable
#         self.__balance = balance

#         # Task 2
#         # insance method

#     def display_balance(self):
#         return f"Your balance is: R{self.__balance:,.2f}"

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#             return f"Withdrawal successful. Your balance is now: R{self.__balance:,.2f}"
#         else:
#             return "Withdrawal failed. Insufficient funds."

#     def deposit(self, amount):
#         if dep_amount > 0:
#             self.__balance += dep_amount
#             return f"Deposit successful. Your balance is now: R{self.__balance:,.2f}"
#         else:
#             return "Deposit failed. Invalid amount."

#     def apply_interest(self):
#         self.__balance = self.__balance + self.__balance * Bank2.interest_rate
#         return f"Interest added. Your balance is now: R{self.__balance:,.2f}"


# gemma = Bank2(123, "Gemma Porril", 15_000)
# dhara = Bank2(124, "Dhara Kara", 50_001)
# caleb = Bank2(125, "Caleb Potts", 100_000)

# gemma.apply_interest()
# dhara.apply_interest()
# caleb.apply_interest()

# print(gemma.display_balance())
# print(dhara.display_balance())
# print(caleb.display_balance())

# print(gemma.display_balance())


# class Bank2:
#     # class variable | All your instances share theclass variables
#     interest_rate = 0.02
#     total_accounts = 0

#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         # Private variable
#         self.__balance = balance
#         Bank2.total_accounts += 1
#         print(self.name, Bank2.total_accounts)

#         # Task 2
#         # insance method

#     @classmethod  # cls -> class
#     def update_interest_rate(cls, rate):
#         Bank2.interest_rate = rate

#     #Static methods -> no cls | normal function
#     @staticmethod
#     def get_total_no_accounts():
#         return f"In total we have {Bank.no_of_accounts} accounts"


#     def display_balance(self):
#         return f"Your balance is: R{self.__balance:,.2f}"

#     # instance method
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#             return f"Withdrawal successful. Your balance is now: R{self.__balance:,.2f}"
#         else:
#             return "Withdrawal failed. Insufficient funds."

#     def deposit(self, amount):
#         if dep_amount > 0:
#             self.__balance += dep_amount
#             return f"Deposit successful. Your balance is now: R{self.__balance:,.2f}"
#         else:
#             return "Deposit failed. Invalid amount."

#     def apply_interest(self):
#         self.__balance = self.__balance + self.__balance * Bank2.interest_rate
#         return f"Interest added. Your balance is now: R{self.__balance:,.2f}"

#     @classmethod
#     def get_total_no_accounts(cls):
#         return cls.total_accounts


# gemma = Bank2(123, "Gemma Porril", 15_000)
# dhara = Bank2(124, "Dhara Kara", 50_001)
# caleb = Bank2(125, "Caleb Potts", 100_000)
# alex = Bank2(126, "Alex Lazarus", 100)


# print(gemma.acc_no)  # public
# # print(gemma.__balance) error | private
# print(gemma.display_balance())

# Bank2.update_interest_rate(0.10)

# # Apply interest
# alex.apply_interest()
# print(alex.display_balance())

# # Task
# # print(Bank2.get_total_no_accounts())  # In total we should have 4 accounts
# print(Bank2.get_total_no_accounts())


# Task 1
# class Circle:
#     pi = 3.14159 #class variable

# #circle1 = Circle(2)
# #print(circle1.calculate_area()) ->
# circle_from_dia = Circle.from_diameter(10)
# #circle_from_dia.calculate_area()


# class Circle:
#     pi = 3.14159  # Class variable

#     def __init__(self, radius):
#         self.radius = radius

#     @classmethod
#     def from_diameter(cls, diameter):
#         radius = diameter / 2
#         return cls(radius)

#     def calculate_area(self):
#         return self.pi * self.radius**2


# circle1 = Circle(2)
# print(circle1.calculate_area())

# circle_from_dia = Circle.from_diameter(10)
# print(circle_from_dia.calculate_area())


# # Task 2 - perimeter
# # static method
# # Circle.perimeter(10) 10 -> radius
# class Circle:
#     pi = 3.14159  # Class variable

#     def __init__(self, radius):
#         self.radius = radius

#     @staticmethod
#     def perimeter(radius):
#         return 2 * Circle.pi * radius


# print(Circle.perimeter(10))


# # Task 3 - combine them
# class Circle:
#     pi = 3.14159  # Class variable

#     def __init__(self, radius):
#         self.radius = radius

#     @classmethod
#     def from_diameter(cls, diameter):
#         radius = diameter / 2
#         return cls(radius)

#     def calculate_area(self):
#         return self.pi * self.radius**2

#     @staticmethod
#     def perimeter(radius):
#         return 2 * Circle.pi * radius


# print(Circle.perimeter(10))


# # Inheritance: Animal(Base/Parent) -> Dog
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Some sound"


# class Dog(Animal):
#     def __init__(self, name, speed):
#         super().__init__(name)
#         self.speed = speed

#     def run(self):
#         return "🐶 wags tail"

#     #Polymorphism | overriding methods
#     def speak(self):
#         return "Woof !! 🐕"

#     def speed_bonus(self):
#         return f"Running at {self.speed *2}km/hr"


# toby = Animal("Toby")
# maxy = Dog("Maxy", 20)

# print(toby.speak())
# print(maxy.name)
# print(maxy.speak())
# print(maxy.run())
# print(maxy.speed_bonus())


# Task Bank
class Bank2:
    # class variable | All your instances share theclass variables
    interest_rate = 0.02
    total_accounts = 0

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        # Potected Variable
        self._balance = balance
        Bank2.total_accounts += 1

        # Task 2
        # insance method

    @classmethod  # cls -> class
    def update_interest_rate(cls, rate):
        Bank2.interest_rate = rate

    # Static methods -> no cls | normal function
    @staticmethod
    def get_total_no_accounts():
        return f"In total we have {Bank.no_of_accounts} accounts"

    def display_balance(self):
        return f"Your balance is: R{self._balance:,.2f}"

    # instance method
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return f"Withdrawal successful. Your balance is now: R{self._balance:,.2f}"
        else:
            return "Withdrawal failed. Insufficient funds."

    def deposit(self, dep_amount):
        if dep_amount > 0:
            self._balance += dep_amount
            return f"Deposit successful. Your balance is now: R{self._balance:,.2f}"
        else:
            return "Deposit failed. Invalid amount."

    def apply_interest(self):
        self._balance = self._balance + self._balance * self.interest_rate
        return f"Interest added. Your balance is now: R{self._balance:,.2f}"

    # def get_balance(self):
    #     return self.__balance


gemma = Bank2(123, "Gemma Porril", 15_000)
dhara = Bank2(124, "Dhara Kara", 50_001)
caleb = Bank2(125, "Caleb Potts", 100_000)
alex = Bank2(126, "Alex Lazarus", 100)


# class SavingsAccount:
#     pass


# class CheckingAccount:
#     pass


# SavingsAccount -  interest_rate = 0.05
# Task 1


class SavingsAccount(Bank2):
    interest_rate = 0.05

    # def __init__(self, acc_no, name, balance):
    #     super().__init__(acc_no, name, balance)

    # def apply_interest(self):
    #     self.balance = self.get_balance()  # Accessing balance using a method
    #     self.balance += self.balance * SavingsAccount.interest_rate
    #     self._Bank2__balance = self.balance
    #     return f"Interest added. Your balance is now: R{self.balance:,.2f}"


gemma = SavingsAccount(123, "Gemma Porrill", 1_000)
gemma.apply_interest()
print(gemma.display_balance())  # 1_050

# Task 2
# CheckingAccount - withdraw  R1
# alex = CheckingAccount(126, "Alex Lazarus", 100)
# alex(50)
#  49


class CheckingAccount(Bank2):
    withdrawal_fee = 1

    def __init__(self, acc_no, name, balance):
        super().__init__(acc_no, name, balance)

    def withdraw(self, amount):
        total_amount = amount + self.withdrawal_fee
        return super().withdraw(total_amount)


alex = CheckingAccount(126, "Alex Lazarus", 100)
print(alex.withdraw(50))


# Magic Methods __repr__ , __str__
class CheckingAccount(Bank2):
    withdrawal_fee = 1

    def __init__(self, acc_no, name, balance):
        super().__init__(acc_no, name, balance)

    def withdraw(self, amount):
        total_amount = amount + self.withdrawal_fee
        return super().withdraw(total_amount)

    """Human readable output"""

    def __str__(self):
        return f"This acount belongs to: {self.name} and has balance of {self._balance}"

    """DeX: """

    def __repr__(self):
        return f"CheckingAccount({self.acc_no}, {self.name}, {self._balance})"

    def __add__(self, other):
        return self._balance + other._balance


alex = CheckingAccount(126, "Alex Lazarus", 100)
print(alex.withdraw(50))
print(alex)

caleb = CheckingAccount(125, "Caleb Potts", 100_000)
print(caleb)

print(repr(alex))
print(repr(caleb))

print(alex + caleb)
