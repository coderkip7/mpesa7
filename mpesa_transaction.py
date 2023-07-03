class Mpesa_Transaction:
    def __init__(self, transaction_id, amount):
        self.transaction_id=transaction_id
        self.amount=amount
    def process_transaction(self):
        raise NotImplementedError("subclass to use this method")

class DepositTransaction(Mpesa_Transaction):
        def process_transaction(self):
            print(f"Deposit_transaction with ID: {self.transaction_id} Processed_Amount: {self.amount}")

class Withdrawal_transaction(Mpesa_Transaction):
    def process_transaction(self):
        print(f"Withdrwal_transaction with ID: {self.transaction_id} processed_Amount: {self.amount}")

class Payment_transaction(Mpesa_Transaction):
    def __init__(self, transaction_id,amount,recepient):
        super().__init__(transaction_id,amount)
        self.recepient = recepient
    def process_transaction(self):
        print(f"Payment transaction with ID: {self.transaction_id} Processed_Amount: {self.amount} Recepient:{self.recepient}")

deposit = DepositTransaction("DHTY","1000Ksh")
deposit.process_transaction()
withdrawal=Withdrawal_transaction("FOFF", "2000ksh")
withdrawal.process_transaction()
payment=Payment_transaction("Mulla", "20000ksh", "Lil-Uzi")
payment.process_transaction()



