print("===== MULTI-CURRENCY TRAVEL BUDGET ANALYSIS =====")

# Enter travel budget
budget = float(input("Enter travel budget in INR: "))

n = int(input("Enter number of expense categories: "))

total_expense = 0
expenses = {}


fee_percent = 2

for i in range(n):
    print("\nExpense Category", i + 1)

    category = input("Enter category name: ")
    amount = float(input("Enter expense amount: "))
    currency = input("Enter currency code: ").upper()
    rate = float(input("Enter exchange rate to INR: "))

    
    converted_amount = amount * rate

    
    fee = converted_amount * fee_percent / 100

    
    final_amount = converted_amount + fee

    total_expense += final_amount

    expenses[category] = final_amount

    print("Category:", category)
    print("Currency:", currency)
    print("Converted Amount: Rs.", round(converted_amount, 2))
    print("Conversion Fee: Rs.", round(fee, 2))
    print("Total Expense: Rs.", round(final_amount, 2))


largest_category = max(expenses, key=expenses.get)
largest_amount = expenses[largest_category]


remaining = budget - total_expense


print("\n========== TRAVEL BUDGET REPORT ==========")

for category, amount in expenses.items():
    print(category, ": Rs.", round(amount, 2))

print("-----------------------------------------")
print("Total Travel Expense: Rs.", round(total_expense, 2))
print("Travel Budget       : Rs.", round(budget, 2))

print("Largest Expense Category:", largest_category)
print("Largest Expense Amount: Rs.", round(largest_amount, 2))

if remaining >= 0:
    print("Remaining Budget: Rs.", round(remaining, 2))
    print("Status: Within Budget")
else:
    print("Budget Exceeded: Rs.", round(abs(remaining), 2))
    print("Status: Over Budget")

print("=========================================")
