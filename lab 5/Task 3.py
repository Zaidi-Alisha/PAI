class Account:
    def __init__(self, account_no, account_bal, security_code):
        self.__account_no = account_no
        self.__account_bal = account_bal
        self.__security_code = security_code

    def print(self):
        print("Account No: ", self.__account_no)
        print("Account Balance: ", self.__account_bal)
        print("Security Code: ", self.__security_code)

account = Account(34568, 4567, 16789)
account.print()
