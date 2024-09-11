class Account:
    '''Private variables'''
    __account_no = None
    __account_bal = None
    __security_code = None

    def set_details(self, account_no, account_bal, security_code):
        self.__account_no = account_no
        self.__account_bal = account_bal
        self.__security_code = security_code

    def display(self):
        print("Account Number: ", self.__account_no)
        print("Account Balance: ",self.__account_bal)
        print("Security Code: ",self.__security_code)

account = Account()
account.set_details(56677557, 767890, 9899)
account.display()
