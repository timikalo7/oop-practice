class InsufficientFundsException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_balance, account_name):
        self.balance = initial_balance
        self.name = account_name
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.get_balance()

    def sufficient_funds(self, amount):
        if self.balance >= amount:
            return
        else:
            raise InsufficientFundsException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.sufficient_funds(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.get_balance()
        except InsufficientFundsException as error:
            print(f'\nWithdraw interrupted: {error}')

    def transfer(self, amount, destination_account):
        try:
            print('\n**********\n\nBeginning Transfer.. 🚀')
            self.sufficient_funds(amount)
            self.withdraw(amount)
            destination_account.deposit(amount)
            print('\nTransfer complete! ✅\n\n**********')
        except InsufficientFundsException as error:
            print(f'\nTransfer interrupted. ❌ {error}')

class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.get_balance()

class SavingsAccount(InterestRewardsAccount):
    def __init__(self, initial_balance, account_name):
        super().__init__(initial_balance, account_name)
        self.withdrawal_fee = 5

    def withdraw(self, amount):
        try:
            self.sufficient_funds(amount + self.withdrawal_fee)
            self.balance = self.balance - (amount + self.withdrawal_fee)
            print("\nWithdraw completed.")
            self.get_balance()
        except InsufficientFundsException as error:
            print(f'\nWithdraw interrupted: {error}')
