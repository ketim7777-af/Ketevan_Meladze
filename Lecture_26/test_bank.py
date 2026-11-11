import pytest
from bank import BankAccount


@pytest.fixture
def account():
    return BankAccount("Keti", 400)


def test_initial_balance(account):
    assert account.balance == 400


def test_deposit_success(account):
    account.deposit(50)
    assert account.balance == 450


@pytest.mark.parametrize("amount", [-50, 0])
def test_deposit_negative(account, amount):
    with pytest.raises(ValueError, match="Amount must be positive"):
        account.deposit(amount)


def test_withdraw_success(account):
    account.withdraw(50)
    assert account.balance == 350


def test_withdraw_insufficient_funds(account):
    with pytest.raises(ValueError, match="Balance is not enough"):
        account.withdraw(450)


@pytest.mark.parametrize("amount", [-50, 0])
def test_withdraw_negative(account, amount):
    with pytest.raises(ValueError, match="Amount must be positive"):
        account.withdraw(amount)