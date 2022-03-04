class Account:
    numberOfAccounts = 0
    amount =  0
    listi = []
    
    def __init__(self,iamount):
        amount = iamount
        Account.numberOfAccounts += 1
        self.number = Account.numberOfAccounts
        Account.listi.append(self)
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
        if self.amount - number < 0:
            IllegalTransfer = ValueError("Account balance to low to transfer that amount")
            raise IllegalTransfer
        else:
            self.amount -= number
            account.amount += number
    
    def total_sum(self):
        sum = 0
        for x in Account.listi:
            sum += x.amount
        return sum
     
    @classmethod
    def reset(cls):
        Account.numberOfAccounts = 0
        Account.amount =  0
        Account.listi = []
