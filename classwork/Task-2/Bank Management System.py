from abc import ABC, abstractmethod
from datetime import datetime

class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def show_details(self):
        print("Name    :", self.name)
        print("Age     :", self.age)
        print("Address :", self.address)

class Customer(Person):

    def __init__(self, name, age, address, customer_id):
        super().__init__(name, age, address)
        self.customer_id = customer_id

class Account(ABC):

    total_accounts = 0

    def __init__(self, number, customer, balance):
        self.number = number
        self.customer = customer
        self.__balance = balance
        self.transactions = []

        Account.total_accounts += 1

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, amount):

        if amount <= 0:
            print("Invalid amount.")
            return

        self.balance = self.balance + amount

        self.transactions.append(f"{datetime.now().strftime('%d-%m-%Y %I:%M %p')}  Deposit Rs. {amount}")

        print("Deposit successful.")
        print("Balance :", self.balance)

    @abstractmethod
    def withdraw(self, amount):
        pass

    @classmethod
    def account_count(cls):
        return cls.total_accounts

    @staticmethod
    def check_number(number):
        return len(str(number)) == 10 and str(number).isdigit()

class SavingsAccount(Account):

    def __init__(self, number, customer, balance, interest):
        super().__init__(number, customer, balance)
        self.interest = interest

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount.")

        elif amount > self.balance:
            print("Insufficient balance.")

        else:
            self.balance = self.balance - amount

            self.transactions.append(f"{datetime.now().strftime('%d-%m-%Y %I:%M %p')} Withdraw Rs. {amount}")

            print("Withdrawal successful.")
            print("Balance :", self.balance)

    def account_type(self):
        return "Savings Account"

    def add_interest(self):

        value = self.balance * self.interest / 100
        self.balance = self.balance + value

        self.transactions.append(f"{datetime.now().strftime('%d-%m-%Y %I:%M %p')}  Interest Rs. {value}")

class CurrentAccount(Account):

    def __init__(self, number, customer, balance, overdraft):
        super().__init__(number, customer, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount.")

        elif amount <= self.balance:
            self.balance = self.balance - amount

            self.transactions.append(f"{datetime.now().strftime('%d-%m-%Y %I:%M %p')}  Withdraw Rs. {amount}")

            print("Withdrawal successful.")
            print("Balance :", self.balance)

        elif amount <= self.balance + self.overdraft:

            extra = amount - self.balance
            self.balance = self.balance - amount
            self.overdraft = self.overdraft - extra

            self.transactions.append(f"{datetime.now().strftime('%d-%m-%Y %I:%M %p')} Withdraw Rs. {amount}")

            print("Withdrawal successful.")
            print("Balance :", self.balance)
            print("Overdraft left :", self.overdraft)

        else:
            print("Amount is more than overdraft limit.")

    def account_type(self):
        return "Current Account"

class PremiumAccount(SavingsAccount):

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount.")

        elif amount > self.balance:
            print("Insufficient balance.")

        else:
            self.balance = self.balance - amount

            self.transactions.append(f"{datetime.now().strftime('%d-%m-%Y %I:%M %p')} Premium Withdraw Rs. {amount}")

            print("Withdrawal successful.")
            print("Balance :", self.balance)

    def account_type(self):
        return "Premium Savings Account"

class Bank:

    def __init__(self):
        self.customers = []
        self.accounts = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, number):

        for account in self.accounts:
            if str(account.number) == str(number):
                return account

        return None

    def create_account(self):

        print("\nCREATE ACCOUNT")

        name = input("Name : ")
        age = int(input("Age : "))
        address = input("Address : ")

        customer_id = "C" + str(len(self.customers) + 1)

        customer = Customer(name, age, address, customer_id)

        number = input("Account number (10 digits) : ")

        while not Account.check_number(number):

            print("Enter a valid 10 digit number.")
            number = input("Account number : ")

        if self.find_account(number) is not None:
            print("Account already exists.")
            return

        balance = float(input("Initial balance : "))

        print("\n1. Savings")
        print("2. Current")
        print("3. Premium Savings")

        choice = input("Choose account type : ")

        if choice == "1":
            account = SavingsAccount(number, customer, balance, 4)

        elif choice == "2":
            account = CurrentAccount(number, customer, balance, 10000)

        elif choice == "3":
            account = PremiumAccount(number, customer, balance, 6)

        else:
            print("Invalid choice.")
            return

        self.add_customer(customer)
        self.add_account(account)

        print("\nAccount created.")
        print("Customer ID :", customer.customer_id)
        print("Account No. :", account.number)
        print("Type        :", account.account_type())
        print("Balance     :", account.balance)

    def deposit_money(self):

        number = input("Account number : ")
        account = self.find_account(number)

        if account is None:
            print("Account not found.")
            return

        amount = float(input("Amount : "))
        account.deposit(amount)

    def withdraw_money(self):

        number = input("Account number : ")
        account = self.find_account(number)

        if account is None:
            print("Account not found.")
            return

        amount = float(input("Amount : "))
        account.withdraw(amount)

    def transfer_money(self):

        sender_number = input("Sender account : ")
        receiver_number = input("Receiver account : ")

        sender = self.find_account(sender_number)
        receiver = self.find_account(receiver_number)

        if sender is None or receiver is None:
            print("Account not found.")
            return

        amount = float(input("Amount : "))

        if amount <= 0:
            print("Invalid amount.")
            return

        if sender.balance < amount:
            print("Insufficient balance.")
            return

        sender.balance -= amount
        receiver.balance += amount

        sender.transactions.append(f"{datetime.now().strftime('%d-%m-%Y %I:%M %p')} Transfer Rs. {amount}")

        receiver.transactions.append(f"{datetime.now().strftime('%d-%m-%Y %I:%M %p')} Received Rs. {amount}")

        print("Transfer successful.")
        print("Sender balance :", sender.balance)

    def show_balance(self):

        number = input("Account number : ")
        account = self.find_account(number)

        if account is None:
            print("Account not found.")
            return

        print("\nCustomer :", account.customer.name)
        print("Customer ID :", account.customer.customer_id)
        print("Account :", account.number)
        print("Type :", account.account_type())
        print("Balance :", account.balance)

    def statement(self):

        number = input("Account number : ")
        account = self.find_account(number)

        if account is None:
            print("Account not found.")
            return

        print("\nAccount Statement")
        print("Customer :", account.customer.name)
        print("Account :", account.number)
        print("Type :", account.account_type())

        print("\nTransactions:")

        if len(account.transactions) == 0:
            print("No transactions.")

        else:
            for item in account.transactions:
                print(item)

        print("Current Balance :", account.balance)

    def __len__(self):
        return len(self.customers)

bank = Bank()

while True:

    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Check Balance")
    print("6. Statement")
    print("7. Total Accounts")
    print("8. Exit")

    choice = input("Enter choice : ")

    if choice == "1":
        bank.create_account()

    elif choice == "2":
        bank.deposit_money()

    elif choice == "3":
        bank.withdraw_money()

    elif choice == "4":
        bank.transfer_money()

    elif choice == "5":
        bank.show_balance()

    elif choice == "6":
        bank.statement()

    elif choice == "7":
        print("Total accounts :", Account.account_count())

    elif choice == "8":
        print("Thank you for using Bank Management System.")
        break

    else:
        print("Invalid choice.")