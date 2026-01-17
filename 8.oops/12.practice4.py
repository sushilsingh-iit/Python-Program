# create a account class with 2 attributes - balance & account no.
# create method for debit ,credit & printing the balance.

# ai method 
class Account:
    def __init__(self, account_no, balance=0):
        """
        Initialize the account with an account number and starting balance.
        """
        self.account_no = account_no
        self.balance = balance

    def debit(self, amount):
        """
        Subtracts the amount from the balance if funds are sufficient.
        """
        if amount > self.balance:
            print(f"Error: Insufficient funds. Balance is {self.balance}")
        else:
            self.balance -= amount
            print(f"Rs. {amount} debited successfully.")

    def credit(self, amount):
        """
        Adds the amount to the balance.
        """
        if amount < 0:
            print("Error: Cannot credit a negative amount.")
        else:
            self.balance += amount
            print(f"Rs. {amount} credited successfully.")

    def print_balance(self):
        """
        Prints the current account details.
        """
        print(f"Account No: {self.account_no} | Current Balance: Rs. {self.balance}")


# --- Example Usage ---

# 1. Create an account with Account No '12345' and starting balance of 1000
my_acc = Account("12345", 1000)

# 2. Check initial balance
my_acc.print_balance()

# 3. Credit (Deposit) money
my_acc.credit(500)
my_acc.print_balance()

# 4. Debit (Withdraw) money
my_acc.debit(200)
my_acc.print_balance()

# 5. Try to debit more than the balance
my_acc.debit(5000)