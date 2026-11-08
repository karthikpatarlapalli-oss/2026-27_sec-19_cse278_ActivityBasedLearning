print("===== MANUFACTURING COST ANALYSIS =====")

# Input details
material = float(input("Enter material cost: "))
labour = float(input("Enter labour charges: "))
wastage_percent = float(input("Enter wastage percentage: "))
machine = float(input("Enter machine cost: "))

quantity = int(input("Enter number of products manufactured: "))
selling_price = float(input("Enter selling price per product: "))
target = float(input("Enter profit target percentage: "))


wastage = material * wastage_percent / 100


total_cost = material + labour + wastage + machine


cost_per_product = total_cost / quantity


revenue = selling_price * quantity


profit = revenue - total_cost


profit_percent = (profit / total_cost) * 100


print("\n===== MANUFACTURING REPORT =====")
print("Material Cost       : Rs.", round(material, 2))
print("Labour Charges      : Rs.", round(labour, 2))
print("Wastage Cost        : Rs.", round(wastage, 2))
print("Machine Cost        : Rs.", round(machine, 2))
print("Total Production Cost:", round(total_cost, 2))
print("Cost Per Product    : Rs.", round(cost_per_product, 2))
print("Total Sales Revenue : Rs.", round(revenue, 2))

if profit >= 0:
    print("Total Profit        : Rs.", round(profit, 2))
else:
    print("Total Loss          : Rs.", round(abs(profit), 2))

print("Profit Percentage   :", round(profit_percent, 2), "%")
print("Target Percentage   :", target, "%")


if profit_percent >= target:
    print("Result: Profit Target Achieved")
else:
    print("Result: Profit Target Not Achieved")

print("=================================")
