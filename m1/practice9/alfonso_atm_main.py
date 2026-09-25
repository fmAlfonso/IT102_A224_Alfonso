import streamlit as st

from alfonso_atm_account import Account
from alfonso_atm_balance import check_balance
from alfonso_atm_deposit import deposit_money
from alfonso_atm_withdraw import withdraw_money
from alfonso_atm_history import view_history
from alfonso_atm_analysis import analyze_transactions

if "account" not in st.session_state:
    st.session_state.account = Account("Juan Dela Cruz", 10000.00)

account = st.session_state.account

st.set_page_config(page_title="ATM App", page_icon="🏧", layout="wide")

st.title("ATM System")
st.write(f"Welcome, {account.account_name}!")
st.divider()

st.sidebar.title("ATM Menu")
choice = st.sidebar.radio(
    "Select an option",
    [
        "Check Balance",
        "Deposit",
        "Withdraw",
        "View History",
        "Analyze Transactions",
    ],
)

if choice == "Check Balance":
    balance = check_balance(account)
    st.subheader("Current Balance")
    st.metric(label="Available Balance", value=f"₱{balance:,.2f}")

elif choice == "Deposit":
    st.subheader("Deposit Money")
    amount = st.number_input(
        "Enter deposit amount",
        min_value=0.00,
        step=100.00,
        format="%.2f",
    )
    if st.button("Deposit Money"):
        if amount <= 0:
            st.error("Invalid amount. Please enter a value greater than zero.")
        elif deposit_money(account, amount):
            st.success(f"Successfully deposited ₱{amount:,.2f}.")
            st.metric("Updated Balance", f"₱{account.check_balance():,.2f}")
        else:
            st.error("Deposit failed.")

elif choice == "Withdraw":
    st.subheader("Withdraw Money")
    st.metric("Available Balance", f"₱{account.check_balance():,.2f}")
    amount = st.number_input(
        "Enter withdrawal amount",
        min_value=0.00,
        step=100.00,
        format="%.2f",
    )
    if st.button("Withdraw Money"):
        if amount <= 0:
            st.error("Invalid amount. Please enter a value greater than zero.")
        elif amount > account.check_balance():
            st.error("Insufficient balance for this withdrawal.")
        elif withdraw_money(account, amount):
            st.success(f"Successfully withdrew ₱{amount:,.2f}.")
            st.metric("Updated Balance", f"₱{account.check_balance():,.2f}")
        else:
            st.error("Withdrawal failed. Check your balance.")

elif choice == "View History":
    st.subheader("Transaction History")
    history = view_history()
    if history:
        transactions = []
        current_transaction = {}

        for line in history.splitlines():
            line = line.strip()
            if not line:
                continue

            if line.startswith("Timestamp:"):
                if current_transaction:
                    transactions.append(current_transaction)
                current_transaction = {"Timestamp": line.split(":", 1)[1].strip()}
            elif line.startswith("Account:"):
                current_transaction["Account"] = line.split(":", 1)[1].strip()
            elif line.startswith("Transaction:"):
                current_transaction["Transaction"] = line.split(":", 1)[1].strip()
            elif line.startswith("Amount:"):
                current_transaction["Amount"] = line.split(":", 1)[1].strip()

        if current_transaction:
            transactions.append(current_transaction)

        if transactions:
            st.table(transactions)
        else:
            st.info("No transaction history available.")
    else:
        st.info("No transaction history available.")

elif choice == "Analyze Transactions":
    st.subheader("Transaction Analysis")
    result = analyze_transactions()

    st.write("### 1. Transaction Summary")
    summary_columns = st.columns(3)
    summary_columns[0].metric("Total Transactions", result["total_transactions"])
    summary_columns[1].metric("Deposits", result["deposits"])
    summary_columns[2].metric("Withdrawals", result["withdrawals"])

    st.divider()
    st.write("### 2. Transaction Amount Analysis")
    amount_columns = st.columns(3)
    amount_columns[0].metric(
        "Total Deposited", f"₱{result['total_deposited']:,.2f}"
    )
    amount_columns[1].metric(
        "Total Withdrawn", f"₱{result['total_withdrawn']:,.2f}"
    )
    amount_columns[2].metric(
        "Average Transaction", f"₱{result['average_transaction']:,.2f}"
    )

    st.divider()
    st.write("### 3. Account Activity Analysis")
    activity_columns = st.columns(3)
    activity_columns[0].metric("Latest Transaction", result["latest_transaction"])
    activity_columns[1].metric(
        "Largest Transaction", f"₱{result['largest_transaction']:,.2f}"
    )
    activity_columns[2].metric("Latest Activity", result["latest_timestamp"])

if False:
    """
    ######### Learning Signature ######### 
    Programmed by: Favio Maximo Alfonso
    Date Submitted: September 25, 2026

    Program Description: This module handles ATM operations and analysis.
    Reflection: I learned how to use steamlit.

    AI Usage
    [ ] No AI Assistance – Completed independently without AI.
    """