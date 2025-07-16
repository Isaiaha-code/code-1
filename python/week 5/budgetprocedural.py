# Set a total budget
total_budget = float(input("Enter your total budget: $"))

# Create a dictionary to track expenses
expenses = {}

def add_expense(category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

def show_summary():
    print("\n--- Budget Summary ---")
    total_spent = sum(expenses.values())
    remaining = total_budget - total_spent

    for category, amount in expenses.items():
        print(f"{category}: ${amount:.2f}")
    
    print(f"\nTotal Spent: ${total_spent:.2f}")
    print(f"Remaining Budget: ${remaining:.2f}")

    if remaining < 0:
        raise ValueError("⚠️ You have exceeded your budget!")


while True:
    print("\nWhat would you like to do?")
    print("1. Add an expense")
    print("2. View summary")
    print("3. Exit")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        category = input("Enter expense category: ")
        try:
            amount = float(input("Enter expense amount: $"))
            add_expense(category, amount)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == "2":
        try:
            show_summary()
        except ValueError as e:
            print(e)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")


