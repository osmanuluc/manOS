class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.category}")
            other_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
            total += item['amount']
        output = title + items + f"Total: {total:.2f}"
        return output

def create_spend_chart(categories):
    category_names = []
    spent = []
    spent_percentages = []

    for category in categories:
        total_spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total_spent += -item['amount']
        spent.append(round(total_spent, 2))
        category_names.append(category.category)

    for amount in spent:
        spent_percentages.append(round(amount / sum(spent), 2) * 100)

    graph = "Percentage spent by category\n"
    labels = range(100, -10, -10)

    for label in labels:
        graph += str(label).rjust(3) + "| "
        for percent in spent_percentages:
            if percent >= label:
                graph += "o  "
            else:
                graph += "   "
        graph += "\n"

    graph += "    ----------\n     "

    longest_name_length = max([len(category) for category in category_names])

    for i in range(longest_name_length):
        for name in category_names:
            if i < len(name):
                graph += name[i] + "  "
            else:
                graph += "   "
        if i < longest_name_length-1:
            graph += "\n     "

    return graph

food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)