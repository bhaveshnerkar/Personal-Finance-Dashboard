
print("Personal Finance Dashboard")
print("Welcome! Let's manage money smarter.")

Expenses = []
income = None

while True:
    print("\nMenu:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Current Balance")
    print("5. View Categories")
    print("6. Exit")

    try:
        ch = int(input("Enter your choice (1-6): "))

        if ch < 1 or ch > 6:
            print("Invalid choice. Enter a number between 1 and 6.")
            continue

    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if ch == 1:
        try:
            amount = float(input("Enter your income amount: "))

            if amount <= 0:
                print("Income must be greater than zero.")
                continue

            income = amount
            print("Income updated successfully!")

        except ValueError:
            print("Invalid income amount.")

    elif ch == 2:
        title = input("Enter the expense title: ").strip()

        if not title:
            print("Title cannot be empty.")
            continue

        cat = input("Enter the expense category: ").strip()

        if not cat:
            print("Category cannot be empty.")
            continue

        try:
            amount = float(input("Enter the expense amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        transaction = {
            "title": title,
            "amount": amount,
            "category": cat
        }

        Expenses.append(transaction)
        print("Expense added successfully!")

    elif ch == 3:
        if not Expenses:
            print("No expenses recorded yet.")
        else:
            print("\nExpenses List:")

            for expense in Expenses:
                print(
                    "Title:", expense["title"],
                    "| Amount:", expense["amount"],
                    "| Category:", expense["category"]
                )

    elif ch == 4:
        if income is None:
            print("Please add income first.")
        else:
            total_expenses = sum(
                expense["amount"] for expense in Expenses
            )

            balance = income - total_expenses
            print("Total Income:", income)
            print("Total Expenses:", total_expenses)
            print("Current Balance:", balance)

    elif ch == 5:
        if not Expenses:
            print("No expense categories available yet.")
        else:
            Categories = {}

            for expense in Expenses:
                category = expense["category"]
                amount = expense["amount"]

                if category in Categories:
                    Categories[category] += amount
                else:
                    Categories[category] = amount

            print("\nCategory-wise Summary:")

            for category, total in Categories.items():
                print(category, ":", total)

    elif ch == 6:
        print("Goodbye!")
        break
