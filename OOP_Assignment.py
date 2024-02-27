class Bank:
  def __init__(self, acc_no, name, balance):
      self.acc_no = acc_no
      self.name = name
      self.balance = balance
      self.transactions = []
      self.transaction_id = 1

  def display_balance(self):
      return f"Your balance is: R{self.balance:,.2f}"

  def withdraw(self, amount, date):
      if amount > 0 and amount <= self.balance:
          self.balance -= amount
          self.transactions.append({'id': self.transaction_id, 'date': date, 'type': 'withdraw', 'amount': amount})
          self.transaction_id += 1
          return f"Withdrawal successful. Your balance is now: R{self.balance:,.2f}"
      else:
          return "Withdrawal failed. Insufficient funds."

  def deposit(self, dep_amount, date):
      if dep_amount > 0:
          self.balance += dep_amount
          self.transactions.append({'id': self.transaction_id, 'date': date, 'type': 'deposit', 'amount': dep_amount})
          self.transaction_id += 1
          return f"Deposit successful. Your balance is now: R{self.balance:,.2f}"
      else:
          return "Deposit failed. Invalid amount."

  def bank_statement(self):
      statement = "id   Date       Type     Amount\n"
      for trans in self.transactions:
          statement += f"{trans['id']:<3} {trans['date']:<9} {trans['type']:<9} {trans['amount']:<6}\n"
      return statement


gemma = Bank(123, "Gemma Porril", 15_000)
dhara = Bank(124, "Dhara Kara", 50_001)
caleb = Bank(125, "Caleb Potts", 100_000)

# Example transactions
gemma.deposit(2000, '29 Feb')
gemma.withdraw(500, '30 Feb')
dhara.withdraw(3000, '1 Mar')
caleb.deposit(5000, '3 Mar')

print("Bank Statement:")
print(gemma.bank_statement())
print(dhara.bank_statement())
print(caleb.bank_statement())
