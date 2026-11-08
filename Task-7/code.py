print("===== RETAIL BILLING SYSTEM =====")

n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0

print("\n----- PRODUCT DETAILS -----")

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category: ").lower()
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    if price < 0 or quantity <= 0:
        print("Invalid price or quantity!")
        continue

    amount = price * quantity

    
    if category == "electronics":
        tax_rate = 18
    elif category == "clothing":
        tax_rate = 5
    elif category == "grocery":
        tax_rate = 0
    else:
        tax_rate = 12

    tax = amount * tax_rate / 100

    subtotal += amount
    total_tax += tax

    print("Product Amount: Rs.", round(amount, 2))
    print("Tax:", tax_rate, "%")
    print("Tax Amount: Rs.", round(tax, 2))


if subtotal >= 5000:
    discount = subtotal * 10 / 100
elif subtotal >= 2000:
    discount = subtotal * 5 / 100
else:
    discount = 0


if discount > 1000:
    discount = 1000


final_amount = subtotal + total_tax - discount

print("\n========== FINAL INVOICE ==========")
print("Subtotal       : Rs.", round(subtotal, 2))
print("Total Tax      : Rs.", round(total_tax, 2))
print("Discount       : Rs.", round(discount, 2))
print("-----------------------------------")
print("Final Amount   : Rs.", round(final_amount, 2))
print("===================================")
print("Thank you! Visit Again.")
