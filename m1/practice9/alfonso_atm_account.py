class Account:

    def __init__(self, name, starting_balance):
        self.account_name = name
        self._balance = starting_balance

    def check_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdrawal(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def withdraw(self, amount):
        return self.withdrawal(amount)

"""
######### Learning Signature ######### 
Programmed by: Favio Maximo Alfonso
Date Submitted: September 25, 2026
 
Program Description: This program allows the user to simulate an ATM that checks balance, deposit and withdrawal. It also uses Account class to create an account with a name and starting balance.
Reflection: I learned how to create and use a simple Account class to manage a bank account.
 
AI Usage
[ ] No AI Assistance – Completed independently without AI.
"""