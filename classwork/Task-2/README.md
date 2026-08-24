Bank Management System
📌 Project Description

This project is a simple Bank Management System developed using Python.

The main purpose of this project is to practice and demonstrate important Object-Oriented Programming (OOP) concepts through a small banking application.

The system allows users to:

Create a new bank account
Deposit money
Withdraw money
Transfer money
Check account balance
View transaction statement
View total number of accounts
Exit the system
🧩 Classes Used

The project contains the following classes:

Person – Stores basic personal information.
Customer – Inherits from Person and stores customer ID.
Account – Abstract base class for bank accounts.
SavingsAccount – Handles savings account operations and interest.
CurrentAccount – Supports overdraft facility.
PremiumAccount – A specialized savings account.
Bank – Manages customers and accounts.
🧠 OOP Concepts Covered
1. Class and Object

Classes are used to create customers, accounts, and bank objects.

2. Constructor

The __init__() method is used to initialize object data.

3. Encapsulation

The account balance is stored as a private attribute:

self.__balance

The @property decorator is used to access and modify the balance.

4. Inheritance

Customer inherits from Person.

SavingsAccount and CurrentAccount inherit from Account.

PremiumAccount inherits from SavingsAccount.

5. Polymorphism

The withdraw() method is implemented differently in different account classes.

6. Abstraction

The Account class uses ABC and @abstractmethod to define an abstract account structure.

7. Class Method

The account_count() class method is used to get the total number of accounts.

8. Static Method

The check_number() static method validates a 10-digit account number.

9. Magic Method

The __len__() method is implemented in the Bank class to return the number of customers.

10. Composition

The Bank class maintains lists of customers and accounts.

💰 Account Types
Savings Account
Allows deposits and withdrawals.
Provides an interest rate.
Does not allow withdrawal beyond the available balance.
Current Account
Allows normal withdrawals.
Provides an overdraft facility up to a specified limit.
Premium Savings Account
Inherits from SavingsAccount.
Provides a different withdrawal behavior.
Uses a higher interest rate.
📋 Menu
===== BANK MANAGEMENT SYSTEM =====

1. Create Account
2. Deposit
3. Withdraw
4. Transfer
5. Check Balance
6. Statement
7. Total Accounts
8. Exit
🧾 Transaction History

The system stores transaction details for each account.

Transactions include:

Deposit
Withdraw
Transfer
Received
Interest