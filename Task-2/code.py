
# Progressive Electricity Billing System

bills = []

n = int(input("Enter number of months: "))

for i in range(n):

    print("\nMonth", i + 1)

    units = float(input("Enter electricity units consumed: "))

    
    if units <= 100:
        energy = units * 2

    elif units <= 200:
        energy = (100 * 2) + (units - 100) * 3

    elif units <= 300:
        energy = (100 * 2) + (100 * 3) + (units - 200) * 5

    else:
        energy = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    
    fixed = 50

  
    surcharge = energy * 0.05

    
    if units < 100:
        rebate = energy * 0.05
    else:
        rebate = 0

    
    total = energy + fixed + surcharge - rebate

    bills.append(total)

    print("Energy Charges: Rs.", round(energy, 2))
    print("Fixed Charges: Rs.", fixed)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Final Bill: Rs.", round(total, 2))



print("\n===== MONTHLY BILL COMPARISON =====")

for i in range(n):
    print("Month", i + 1, "Bill: Rs.", round(bills[i], 2))

    if i > 0:
        increase = bills[i] - bills[i - 1]

        if bills[i - 1] > 0:
            percentage = (increase / bills[i - 1]) * 100
        else:
            percentage = 0

        if percentage > 30:
            print("Unusual Increase Detected!")
        else:
            print("Normal Bill Change")

        print("Bill Change:", round(increase, 2))
        print("Percentage Change:", round(percentage, 2), "%")

print("\nTotal Electricity Bill: Rs.", round(sum(bills), 2))
print("Program Completed")

