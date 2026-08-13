from bank_account import BankAccount

if __name__ == "__main__":
    alice = BankAccount("Alice", 100.0)
    bob = BankAccount("Bob")
    carol = BankAccount("Carol", 50.0)

    alice.deposit(50)
    bob.deposit(200)
    carol.withdraw(20)
    alice.withdraw(30)

    try:
        bob.withdraw(10000)
    except ValueError as e:
        print(f"Expected error: {e}")

    print(alice)
    print(bob)
    print(carol)