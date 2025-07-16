from budget import Budget

# Step 1: Create an instance of the Budget class with $2500
my_budget = Budget(2500)

try:
    my_budget.add_item("Rent", 1200)
    my_budget.add_item("Groceries", 300)
    my_budget.add_item("Transportation", 150)
    my_budget.add_item("Phone Bill", 100)
except ValueError as e:
    print("Error:", e)

my_budget.show_budget()



