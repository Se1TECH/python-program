# Expense tracker in python

import csv
import datetime


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def addExpense(self, amount, category, description):
        expense = {
            'date': datetime.datetime.now().strftime("%Y-%m-%d"),
            'amount': amount,
            'category': category,
            'description': description
        }
        self.expenses.append(expense)
        print("Expend Added Successfully.")

    def viewExpense(self):
        if not self.expenses:
            print("NO expense found.")
        else:
            print("\n--- Expenses ---")
            for expense in self.expenses:
                print(
                    f"Date: {expense['date']}, Amount: {expense['amount']}, Category {expense['category']}, Description: {expense['description']}  ")

    def analyzeExpenses(self):
        total_expenses = sum(expense['amount'] for expense in self.expenses)
        categories = set(expense['category'] for expense in self.expenses)
        category_totals = {category: sum(
            expense['amount'] for expense in self.expenses if expense['category'] == category) for category in categories}

        print("Expense Analysis:")
        print("Total Expenses:", total_expenses)
        print("Category-wise Expenses:")
        for category, amount in category_totals.items():
            print(f"{category}: {amount}")


def saveExpenses(expenses):
    with open('expenses.csv', 'w', newline='') as file:
        writer = csv.DictWriter(
            file, fieldnames=['date', 'amount', 'category', 'description'])
        writer.writeheader()
        writer.writerows(expenses)


def loadExpenses():
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []


def main():
    expense_tracker = ExpenseTracker()
    expense_tracker.expenses = loadExpenses()

    while True:
        print("\n----- Expense Tracker -----")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Analyze Expense")
        print("4. Exit")
        choice = input("Enter Your Choice: ")

        if choice == "1":
            amount = float(input("Enter the expense amount: "))
            category = input("Enter Expense Category: ")
            description = input("Enter a Description: ")
            expense_tracker.addExpense(amount, category, description)

        elif choice == "2":
            expense_tracker.viewExpense()

        elif choice == "3":
            expense_tracker.analyzeExpenses()

        elif choice == "4":
            saveExpenses(expense_tracker.expenses)
            break

        else:
            print("Invalid Choice. Please Try Again.")


if __name__ == "__main__":
    main()
