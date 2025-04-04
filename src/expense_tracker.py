import csv
import os
from datetime import datetime

expenses = []
budget = 0.0
FILENAME = os.path.join('data', 'expenses.csv')

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Travel): ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
        amount = float(amount)
    except ValueError:
        print("Invalid date or amount format. Please try again.")
        return

    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }
    expenses.append(expense)
    print("Expense added successfully.")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- All Expenses ---")
    for expense in expenses:
        if all(k in expense for k in ['date', 'category', 'amount', 'description']):
            print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")
        else:
            print("Incomplete entry found and skipped.")

def set_budget():
    global budget
    try:
        budget = float(input("Enter your monthly budget: "))
        print(f"Monthly budget set to {budget}")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def track_budget():
    total_expense = sum(exp['amount'] for exp in expenses)
    print(f"Total expenses so far: {total_expense}")
    if budget == 0:
        print("No budget set yet. Use 'Set Budget' option.")
    elif total_expense > budget:
        print("Warning: You have exceeded your budget!")
    else:
        print(f"You have {budget - total_expense} left for the month.")

def save_expenses():
    os.makedirs(os.path.dirname(FILENAME), exist_ok=True)  # <-- Ensure directory exists
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        writer.writerows(expenses)
    print(f"Expenses saved to {FILENAME}.")

def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    row['amount'] = float(row['amount'])
                    expenses.append(row)
                except ValueError:
                    print("Skipped a row with invalid amount format.")
        print(f"Loaded {len(expenses)} expenses from {FILENAME}.")
    else:
        print("No saved expense file found.")

def menu():
    load_expenses()
    while True:
        print("\n--- Personal Expense Tracker Menu ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Track budget")
        print("4. Save expenses")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            if budget == 0:
                set_budget()
            track_budget()
        elif choice == '4':
            save_expenses()
        elif choice == '5':
            save_expenses()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    menu()
