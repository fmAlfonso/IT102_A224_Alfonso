def analyze_transactions():
    try:
        with open("transactions.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        return {
            "total_transactions": 0,
            "deposits": 0,
            "withdrawals": 0,
            "total_deposited": 0,
            "total_withdrawn": 0,
            "average_transaction": 0,
            "latest_transaction": "None",
            "latest_timestamp": "None",
            "largest_transaction": 0,
        }

    transactions = []
    current = {}

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue

        if line.startswith("Timestamp:"):
            current["timestamp"] = line.split(":", 1)[1].strip()
        elif line.startswith("Account:"):
            current["account"] = line.split(":", 1)[1].strip()
        elif line.startswith("Transaction:"):
            current["transaction"] = line.split(":", 1)[1].strip()
        elif line.startswith("Amount:"):
            current["amount"] = float(line.split(":", 1)[1].strip())

        if all(key in current for key in ("timestamp", "account", "transaction", "amount")):
            transactions.append(current.copy())
            current = {}

    if not transactions:
        return {
            "total_transactions": 0,
            "deposits": 0,
            "withdrawals": 0,
            "total_deposited": 0,
            "total_withdrawn": 0,
            "average_transaction": 0,
            "latest_transaction": "None",
            "latest_timestamp": "None",
            "largest_transaction": 0,
        }

    total_transactions = len(transactions)

    deposits = sum(
        1 for t in transactions
        if t["transaction"].lower() in {"deposit", "deposited"}
    )

    withdrawals = sum(
        1 for t in transactions
        if t["transaction"].lower() in {"withdraw", "withdrawal", "withdrawn"}
    )

    total_deposited = sum(
        float(t["amount"]) for t in transactions
        if t["transaction"].lower() in {"deposit", "deposited"}
    )

    total_withdrawn = sum(
        float(t["amount"]) for t in transactions
        if t["transaction"].lower() in {"withdraw", "withdrawal", "withdrawn"}
    )

    largest_transaction = max(
        (float(t["amount"]) for t in transactions),
        default=0
    )

    latest_transaction = transactions[-1]["transaction"].title()
    latest_timestamp = transactions[-1]["timestamp"]

    average_transaction = (
        sum(float(t["amount"]) for t in transactions) / total_transactions
        if total_transactions else 0
    )

    return {
        "total_transactions": total_transactions,
        "deposits": deposits,
        "withdrawals": withdrawals,
        "total_deposited": total_deposited,
        "total_withdrawn": total_withdrawn,
        "average_transaction": average_transaction,
        "latest_transaction": latest_transaction,
        "latest_timestamp": latest_timestamp,
        "largest_transaction": largest_transaction,
    }

"""
######### Learning Signature ######### 
Programmed by: Favio Maximo Alfonso
Date Submitted: September 25, 2026

Program Description: This module analyzes ATM transaction data.
Reflection: I learned how to process and analyze transaction data to extract meaningful insights.

AI Usage
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""