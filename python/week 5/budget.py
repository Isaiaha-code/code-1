funds = 2500

budgets = {}


# budget.py

class Budget:
    def __init__(self, funds):
        self.funds = funds
        self.budgets = {}

    def add_item(self, item_name, amount):
        if amount > self.funds:
            raise ValueError("Not enough funds!")
        self.budgets[item_name] = amount
        self.funds -= amount

    def show_budget(self):
        print("Remaining funds:", self.funds)
        print("Budget breakdown:")
        for item, amount in self.budgets.items():
            print(f"{item}: ${amount}")


           

from budget import Budget

my_budget = Budget(2500)

my_budget.add_item("Rent", 1200)
my_budget.add_item("Groceries", 300)


my_budget.show_budget()

 



