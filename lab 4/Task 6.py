class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance is ${self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("You cannot withdraw due to insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} have been withdrawn. New balance is ${self.balance}.")

    def check_balance(self):
        print("Balance: $ ", self.balance)

account = BankAccount(345678, 7543, "2024-09-11", "Alisha")
account.deposit(1239)
account.withdraw(4324)
account.check_balance()

