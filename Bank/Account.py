class Account:
    numberOfAccounts = 0
    
    
    def __init__(self,amount):
        Account.numberOfAccounts += 1
        self.number = Account.numberOfAccounts
        self.amount = amount
        
    def withdraw(self, number):
        self.amount -= number
    
    @classmethod
    def reset(cls):
        Account.numberOfAccounts = 0
