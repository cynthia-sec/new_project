import random
import os

class BankAccount:
    def __init__(self, username, account_type, balance=0):
        self.username = username
        self.account_type = account_type
        self.balance = balance

        # generate unique ID
        self.account_id = random.randint(10000, 99999)

        # create statement file
        self.filename = f"{self.username}_{self.account_type}_{self.account_id}.txt"

        with open(self.filename, "w") as f:
            f.write(f"Account created for {self.username}\n")
            f.write(f"Account type: {self.account_type}\n")
            f.write(f"Starting balance: {self.balance}\n\n")

    # ---------- deposit ----------
    def deposit(self, amount):
        self.balance += amount
        with open(self.filename, "a") as f:
            f.write(f"Deposited: {amount}, Balance: {self.balance}\n")

    # ---------- withdraw ----------
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
            return

        self.balance -= amount
        with open(self.filename, "a") as f:
            f.write(f"Withdrew: {amount}, Balance: {self.balance}\n")

    # ---------- balance ----------
    def get_balance(self):
        return self.balance

    # ---------- getters ----------
    def get_account_id(self):
        return self.account_id

    def get_username(self):
        return self.username

    def get_account_type(self):
        return self.account_type

    # ---------- transaction history ----------
    def get_transaction_history(self):
        with open(self.filename, "r") as f:
            return f.read()


# ---------- TESTING ----------
def main():
    acc1 = BankAccount("Cynthia", "savings", 100)

    acc1.deposit(50)
    acc1.withdraw(30)

    print("Balance:", acc1.get_balance())
    print("Account ID:", acc1.get_account_id())
    print("Username:", acc1.get_username())
    print("Account Type:", acc1.get_account_type())

    print("\nTransaction History:\n")
    print(acc1.get_transaction_history())


main()