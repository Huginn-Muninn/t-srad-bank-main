class Account:
    numberOfAccounts = 0
    
    def __init__(self):
        Account.numberOfAccounts += 1
        Account.amount = 2500
        self.number = Account.numberOfAccounts
        self.amount = Account.amount
    
    @classmethod
    def reset(cls):
        Account.numberOfAccounts = 0
