class Account:
    numberOfAccounts = 0
    startamount= 2500
    
    def __init__(self):
        Account.numberOfAccounts += 1
        self.number = Account.numberOfAccounts
        self.amount = Account.startamount
    
    @classmethod
    def reset(cls):
        Account.numberOfAccounts = 0
