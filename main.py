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
    print("5. Exit")

    try:
        ch = int(input("Enter your choice (1-5):"))
        if ch <1 or ch >5 :
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue    
    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 5.")
        continue


    if ch == 1:
        income= float(input("Enter the income amount:" +"\n"))
        print("Income updated sucessfully.")
    elif ch == 2:
        title=input("Enter the Expenses title:")
        if not title:
            print("Title cannot be empty. Please try again.")
            continue
        try:
            amount= float(input("Enter the Expenses amount:"))
            if amount<= 0:
                print("Amount must be greater than zero.")
                continue
        except ValueError:
            print("----------------------------------------------")
            print("Invalid Amount. Please enter a valid  number! ")
            print("----------------------------------------------")
            continue
        cat=input("Enter the Expenses category:")
        print("Expenses:",title)
        print("Amount:",amount)
        print("Category:",cat)

        tansation = {"title": title, "amount": amount, "category": cat}
        Expenses.append(tansation)

    elif ch == 3:
        if not Expenses:
            print("No Expenses recorded yet!")
        else:
            print("Expenses List:")
            for expense in Expenses:
                print("Title:", expense["title"], "=", expense["amount"], "Category:", expense["category"]      )

    elif ch == 4:
        if income is None:
            print("Income not recorded yet!")
            continue    
        balance=income-sum(expense["amount"] for expense in Expenses)
        if balance is None:
            print("balance not recorded yet !")
        else:
            print("current balance:",balance)

    elif ch == 5:
        print("Goodbye!")
        break
