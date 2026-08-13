"""Tests for the BankAccount class."""

import pytest

from bank_account import BankAccount


def test_deposit_increases_balance():
    """Depositing a positive amount should increase the balance."""
    account = BankAccount("Alice", 100.0)
    account.deposit(50)
    assert account.balance == 150.0


def test_withdraw_decreases_balance():
    """Withdrawing a valid amount should decrease the balance."""
    account = BankAccount("Alice", 100.0)
    account.withdraw(30)
    assert account.balance == 70.0


def test_withdraw_insufficient_funds_raises():
    """Withdrawing more than the balance should raise ValueError."""
    account = BankAccount("Bob", 100.0)
    with pytest.raises(ValueError):
        account.withdraw(200)


def test_repr_format():
    """__repr__ should return the expected formatted string."""
    account = BankAccount("Carol", 50.0)
    assert repr(account) == "BankAccount(owner='Carol', balance=50.0)"


def test_withdraw_negative_amount_raises():
    """Withdrawing a negative amount should raise ValueError."""
    account = BankAccount("Dave", 100.0)
    with pytest.raises(ValueError):
        account.withdraw(-10)


def test_deposit_negative_amount_raises():
    """Depositing a negative amount should raise ValueError."""
    account = BankAccount("Eve", 100.0)
    with pytest.raises(ValueError):
        account.deposit(-10)


def test_init_negative_balance_raises():
    """Creating an account with a negative initial balance should raise ValueError."""
    with pytest.raises(ValueError):
        BankAccount("Frank", -100.0)