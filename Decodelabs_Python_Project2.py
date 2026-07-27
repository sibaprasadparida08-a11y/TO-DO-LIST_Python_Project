expenses = []

total_spent = 0.0

def add_expense():
    global total_spent
    try:
        amount = float(input("\nEnter Expense Amount (₹) 👉 : "))
        if amount <= 0:
            print("❌ Expense amount must be greater than zero .")
            return
        expenses.append(amount)
        total_spent = total_spent + amount
        print("✅ Expense Added Successfully!")
    except ValueError:
        print("❌ Invalid input ! Please enter a valid number .")

def view_expenses():
    if len(expenses) == 0:
        print("\n🫙 No expenses recorded .")
        return
    print("\n========== Expense History ==========")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. ₹{expense:.2f}")

    print("=====================================")

def show_total():
    print("\n========== Total Spent ==========")
    print(f"Total Expenses = ₹{total_spent:.2f}")
    print("=================================")

def menu():
    print("\n")
    print("=" * 50)
    print("         EXPENSE TRACKER APPLICATION 🈸")
    print("=" * 50)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spent")
    print("4. Exit")
    print("=" * 50)

print("=" * 50)
print("     WELCOME TO MY EXPENSE TRACKER APPLICATION")
print("=" * 50)

while True:

    menu()

    choice = input("Enter your choice (1-7) : ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        show_average()

    elif choice == "5":
        highest_expense()

    elif choice == "6":
        lowest_expense()

    elif choice == "7":
        print("\nThank you for using My Expense Tracker Application .")
        print("Visit again...See you again... 🙋 !")
        print("Have a Nice Day ☺️  !")
        break

    else:
        print("❌ Invalid Choice ! Please choice between 1 to 4 .")