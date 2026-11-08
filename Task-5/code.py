
# Multi-Plan Telecommunications Cost Optimization

print("===== MOBILE PLAN OPTIMIZATION SYSTEM =====")


data = float(input("Enter required data usage (GB): "))
calls = int(input("Enter required call minutes: "))
validity = int(input("Enter required validity days: "))
budget = float(input("Enter your budget (Rs.): "))


plans = [
    {"name": "Plan A", "price": 199,
     "data": 2, "calls": 200, "days": 28},

    {"name": "Plan B", "price": 299,
     "data": 5, "calls": 500, "days": 56},

    {"name": "Plan C", "price": 399,
     "data": 10, "calls": 1000, "days": 84},

    {"name": "Plan D", "price": 499,
     "data": 15, "calls": 1500, "days": 90}
]

eligible = []


if data < 0 or calls < 0 or validity <= 0 or budget < 0:
    print("Invalid Input!")

else:

    print("\n===== PLAN COMPARISON =====")

    for p in plans:

        
        extra_data = max(0, data - p["data"])
        extra_calls = max(0, calls - p["calls"])

        
        data_charge = extra_data * 20
        call_charge = extra_calls * 1

        
        total = p["price"] + data_charge + call_charge

        print("\n", p["name"])
        print("Plan Price: Rs.", p["price"])
        print("Extra Data Charge: Rs.", data_charge)
        print("Extra Call Charge: Rs.", call_charge)
        print("Total Cost: Rs.", total)

        
        if p["days"] >= validity and total <= budget:

            eligible.append({
                "name": p["name"],
                "cost": total,
                "days": p["days"]
            })

    
    print("\n===== BEST MOBILE PLAN =====")

    if len(eligible) > 0:

        best = min(eligible, key=lambda x: x["cost"])

        print("Best Plan:", best["name"])
        print("Total Cost: Rs.", best["cost"])
        print("Validity:", best["days"], "days")
        print("Status: Eligible")

    else:
        print("No suitable plan found!")
        print("Please increase your budget or reduce usage.")

    print("\nProgram Completed Successfully!")

