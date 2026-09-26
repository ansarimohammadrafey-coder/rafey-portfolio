print("===== Expense Tracker =====")

expenses = []
total = 0

while True:
    print("\n1. Add Expense")
    print("2. Show Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append((name, amount))
        total += amount

        print("Expense added successfully!")

    elif choice == "2":
        print("\n===== Expenses =====")

        if not expenses:
            print("No expenses added.")
        else:
            for name, amount in expenses:
                print(name, ":", amount)

            print("Total Expense:", total)

    elif choice == "3":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")