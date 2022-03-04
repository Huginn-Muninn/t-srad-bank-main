class Account:
    numberOfAccounts = 0
    NegativeBalanceNotAllowed = ValueError("B positive :)")
    
    def __init__(self,amount):
        Account.numberOfAccounts += 1
        self.number = Account.numberOfAccounts
        if amount < 0:
            NegativeBalanceNotAllowed = ValueError("Negative Balance Is Not Allowed")
            raise NegativeBalanceNotAllowed
        else:
            self.amount = amount
       
    def __str__ (self):
        return str(self.number).zfill(6)
        
    def withdraw(self, number):
        if self.amount - number < 0:
            IllegalWithdrawal = ValueError("Account balance to low to withdraw that amount")
            raise IllegalWithdrawal
        else:
            self.amount -= number

    def deposit(self, number):
        self.amount += number
        
    def transfer(self, number, account):
        self.amount -= number
        account.amount += number
     
    @classmethod
    def reset(cls):
        Account.numberOfAccounts = 0
        