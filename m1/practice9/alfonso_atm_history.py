def view_history():
    try:
        with open("transactions.txt", "r") as file:
            lines = file.read()
            return lines
    except FileNotFoundError:
        return []


"""
######### Learning Signature ######### 
Programmed by: Favio Maximo Alfonso
Date Submitted: September 25, 2026

Program Description: This module handles viewing transaction history for an ATM account.
Reflection: I learned how to do basic file handling in Python.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
"""