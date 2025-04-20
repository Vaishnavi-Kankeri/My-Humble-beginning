class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance 

  def deposit(self, amount):
    self.balance = self.balance + amount
    return self.balance

  def withdraw(self, amount):
    self.balance = self.balance - amount
    return self.balance

  def display_balance(self):
    print('the current balance is ' + str(self.balance))

Raman = BankAccount('Raman', 'Vyankatesh', 112233, 'B1', 17080304, 0)

Raman.deposit(int(input("Enter the amount you wanna deposit: ")))
Raman.withdraw(int(input("Enter the amount you wanna withdraw: ")))
Raman.display_balance()