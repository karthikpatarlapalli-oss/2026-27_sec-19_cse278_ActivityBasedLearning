
# Railway Fare and Reservation Calculator

print("===== RAILWAY FARE CALCULATOR =====")

n = int(input("Enter number of passengers: "))

total_amount = 0

for i in range(n):

    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))
    distance = float(input("Enter travel distance (km): "))

    print("1. Sleeper")
    print("2. AC 3 Tier")
    print("3. AC 2 Tier")

    choice = int(input("Select travel class: "))

    
    if age < 0 or distance <= 0 or choice not in [1, 2, 3]:
        print("Invalid passenger details!")
        continue

    
    if distance <= 100:
        base = distance * 2

    elif distance <= 200:
        base = (100 * 2) + (distance - 100) * 1.5

    else:
        base = (100 * 2) + (100 * 1.5) + (distance - 200) * 1

    
    if choice == 1:
        class_name = "Sleeper"
        class_charge = 100

    elif choice == 2:
        class_name = "AC 3 Tier"
        class_charge = 300

    else:
        class_name = "AC 2 Tier"
        class_charge = 500

    # Age-based concession
    if age < 5:
        concession = base
    elif age <= 12:
        concession = base * 0.50
    elif age >= 60:
        concession = base * 0.20
    else:
        concession = 0

    
    fare = base - concession + class_charge

    
    if age < 5:
        fare = 0

    reservation = 50

    if age < 5:
        reservation = 0

    total = fare + reservation

    print("\nTicket Details")
    print("Passenger Name:", name)
    print("Age:", age)
    print("Travel Class:", class_name)
    print("Base Fare: Rs.", round(base, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Class Charge: Rs.", class_charge)
    print("Reservation Fee: Rs.", reservation)

    
    cancel = input("Cancel ticket? (yes/no): ").lower()

    if cancel == "yes":
        penalty = total * 0.25
        refund = total - penalty

        print("Cancellation Penalty: Rs.", round(penalty, 2))
        print("Refund Amount: Rs.", round(refund, 2))

        total = 0

    else:
        print("Ticket Confirmed!")
        print("Final Ticket Fare: Rs.", round(total, 2))

        total_amount += total

print("\n===== FINAL SUMMARY =====")
print("Total Confirmed Ticket Amount: Rs.",
      round(total_amount, 2))

print("Program Completed Successfully!")

