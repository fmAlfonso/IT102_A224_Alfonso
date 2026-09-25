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
    amount = st.number_input("Enter withdrawal amount", min_value=0.00, step=100.00)
    if st.button("Withdraw Money"):
        if amount <= 0:
            st.warning("Enter an amount greater than zero.")
        elif withdraw_money(account, amount):
            st.success(f"Successfully withdrew ₱{amount:,.2f}.")
            st.metric("New Balance", f"₱{account.check_balance():,.2f}")
        else:
            st.error("Withdrawal failed. Check your balance.")

elif choice == "View History":
    st.subheader("Transaction History")
    history = view_history()
    if history:
        st.text_area("History", history, height=300)
    else:
        st.info("No transaction history available.")

elif choice == "Analyze Transactions":
    st.subheader("Transaction Analysis")
    result = analyze_transactions()
    st.json(result)

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