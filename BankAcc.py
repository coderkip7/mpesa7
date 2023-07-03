class BankAccount:
    def __init__(self,account_number,holder_name,balance=0):
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance=balance
    def deposit(self,amount):
        self.balance +=amount
    def withdrawal(self,amount):
        if self.balance>= amount:
            self.balance-=amount
        else:
            print("insufficient funds")
    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name : {self.holder_name}")
        print(f"Balance : {self.balance}")
my_account=BankAccount("12345678ms","21-Savage",8000000)
my_account.display_balance()
my_account.deposit(5000)
my_account.display_balance()
my_account.withdrawal(9500000)
my_account.display_balance()
