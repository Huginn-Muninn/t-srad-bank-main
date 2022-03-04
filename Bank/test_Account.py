import pytest
from .Account import Account

@pytest.fixture(autouse=True)
def run_around_tests():
    yield
    # We need to reset the Account class variables between tests.
    Account.reset()

def test_first_account_gets_number_1():
    account = Account(2500)
    assert account.number == 1

@pytest.fixture
def two_accounts():
    Account(2500)
    Account(2500)

def test_number_of_accounts_increases_on_creation(two_accounts):
    assert Account.numberOfAccounts == 2

# Write your tests below here.
def test_amount_start():
    account1 = Account(2500)
    assert account1.amount == 2500
    
def test_withdraw():
    account = Account(2500)
    account.withdraw(1500)
    assert account.amount == 1000
    
def test_deposit():
    account = Account(2500)
    account.deposit(1500)
    assert account.amount == 4000

def test_transfer():
    account1 = Account(2500)
    account2 = Account(2500)
    account1.transfer(1000,account2)
    assert account1.amount + account2.amount == 5000
    assert account1.amount == 1500
    assert account2.amount == 3500

def test_str():
    account = Account(2500)
    assert account.__str__() == "000001"
    
    