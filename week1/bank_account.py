"""Bank acconut management module."""

class BankAccount:
    """A simple bank account that supports deposits and withdrawals.

    Attributes
    ----------
        owner: The name of the account holder.
        balance: The current balance of the account.

    """

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        """Initialize a BankAccount.

        Args:
        ----
            owner: The name of the account holder.
            balance: The starting balance. Defaults to 0.0.

        Raises:
        ------
            ValueError: If the initial balance is negative.

        """
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> float:
        """Deposits money into the account.

        Args:
        ----
            amount: The amount to deposit. Must be positive.

        Returns:
        -------
            The updated balance after the deposit.

        Raises:
        ------
            ValueError: If the amount is negative or zero.

        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """Withdraws money from the account.

        Args:
        ----
            amount: The amount to withdraw. Must be positive and
                not exceed the current balance.

        Returns:
        -------
            The updated balance after the withdrawal.

        Raises:
        ------
            ValueError: If the amount is negative, zero, or exceeds
                the current balance.

        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for this withdrawal.")
        self.balance -= amount
        return self.balance

    def __repr__(self) -> str:
        """Return a string representation of the account.

        Return:
        ------
            A string in the format 'BankAccount(owner=..., balance=...)'.

        """
        return f"BankAccount(owner={self.owner!r}, balance={self.balance})"