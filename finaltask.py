from abc import ABC, abstractmethod
from functools import reduce
from datetime import datetime


class Account(ABC):
    @abstractmethod
    def get_summary(self):
        pass
class User(Account):
    def _init_(self, user_id, name):
        self._user_id = user_id  
        self._name = name
        self.expenses = []

    def get_summary(self):
        return f"User: {self._name} (ID: {self._user_id})"

class Expense(User):
    def _init_(self, user_id, name):
        super()._init_(user_id, name)
    def get_summary(self):
        base_info = super().get_summary()
        return f"{base_info} - Total Transactions: {len(self.expenses)}"

    def add_expense(self, amount, category, description, date):
        
        expense_item = {
            "amount": float(amount),
            "category": category,
            "description": description,
            "date": date 
        }
        self.expenses.append(expense_item)
    
    def view_all_expenses(self):
        return [f"{self._name} spent {e['amount']} on {e['category']}" for e in self.expenses]

    def filter_by_category(self, category):
        return list(filter(lambda x: x['category'].lower() == category.lower(), self.expenses))

    def calculate_total(self):
        if not self.expenses: return 0
        amounts = list(map(lambda x: x['amount'], self.expenses))
        return reduce(lambda a, b: a + b, amounts)

    def category_report(self):
        categories = set(e['category'] for e in self.expenses)
        
        return {cat: sum(e['amount'] for e in self.expenses if e['category'] == cat) for cat in categories}

    def get_highest_expense(self):
        if not self.expenses: return None
        return reduce(lambda a, b: a if a['amount'] > b['amount'] else b, self.expenses)
    def monthly_report(self, month_str):
        monthly_list = [e for e in self.expenses if e['date'].startswith(month_str)]
        total = sum(e['amount'] for e in monthly_list)
        return total

    def get_smart_insight(self):
        report = self.category_report()
        insights = []
        for cat, amt in report.items():
            if cat.lower() == "food" and amt > 5000:
                insights.append("⚠️ Smart Insight: You are spending too much on Food this month!")
            if cat.lower() == "shopping" and amt > 10000:
                insights.append("⚠️ Smart Insight: Consider cutting down on Shopping.")
        return insights if insights else ["✅ Spending is within healthy limits."]
    
manager = Expense(101, "swetha")
manager.add_expense(2000, "Food", "Dinner at Bistro", "2025-10-05")
manager.add_expense(1500, "Travel", "Uber rides", "2025-10-06")
manager.add_expense(4000, "Food", "Grocery Stockup", "2025-10-10")
manager.add_expense(3000, "Shopping", "New Jeans", "2025-10-12")
print(manager.get_summary())
print(f"Total Spending: {manager.calculate_total()}")
print("Category Wise:", manager.category_report())
highest = manager.get_highest_expense()
print(f"Highest Single Expense: {highest['amount']} ({highest['description']})")

for insight in manager.get_smart_insight():
    print(insight)