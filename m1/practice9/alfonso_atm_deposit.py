from datetime import datetime
def deposit_money(account, amount):
    if amount <= 0:
        return False
    success = account.deposit(amount)

    if success:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("transactions.txt", "a") as file:
            file.write(f"Timestamp: {timestamp}\n")
            file.write(f"Account: {account.account_name}\n")
            file.write("Transaction: Deposit\n")
            file.write(f"Amount: ₱{amount:.2f}\n")
        return True
    return False

"""
######### Learning Signature ######### 
Programmed by: Favio Maximo Alfonso
Date Submitted: September 25, 2026

Program Description: This module handles deposit transactions for an ATM account and logs them.
Reflection: I learned how to implement transaction logic and file handling in Python.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
"""