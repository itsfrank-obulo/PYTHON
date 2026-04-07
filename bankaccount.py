class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance=0):
        # Private attributes (indicated by underscores)
        self._account_holder = account_holder
        self._account_number = account_number
        self._balance = initial_balance

    # Property for account_number: Read-only
    @property
    def account_number(self):
        return self._account_number

    # Property for balance: Includes a getter
    @property
    def balance(self):
        return self._balance

    # Setter for balance: Includes validation logic
    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Error: Balance cannot be negative.")
        else:
            self._balance = value

    def deposit(self, amount):
        """Adds money to the account if the amount is positive."""
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deducts money if funds are sufficient and amount is positive."""
        if amount > self._balance:
            print("Error: Insufficient funds.")
        elif amount <= 0:
            print("Error: Withdrawal amount must be positive.")
        else:
            self._balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self._balance}")

    def get_balance(self):
        """Returns the current balance."""
        return self._balance

# --- Testing the System ---

# 1. Initialize account
my_account = BankAccount("Alice Smith", "123456789", 500)

# 2. Accessing properties
print(f"Account Holder: {my_account._account_holder}")
print(f"Account Number: {my_account.account_number}")

# 3. Trying to change account number (This would require a setter, which we didn't add)
# my_account.account_number = "999" # This would raise an AttributeError

# 4. Deposits and Withdrawals
my_account.deposit(200)   # Valid deposit
my_account.deposit(-50)   # Invalid deposit

my_account.withdraw(100)  # Valid withdrawal
my_account.withdraw(1000) # Invalid: Insufficient funds

# 5. Using the balance setter/getter
print(f"Final Balance: ${my_account.get_balance()}")