
import math

print("CAMPUS EVENT FINANCIAL PLANNING")


venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificate = float(input("Enter certificate cost: "))


participants = int(input("Enter expected participants: "))
sponsorship = float(input("Enter sponsorship amount: "))
fee = float(input("Enter registration fee per participant: "))


total_cost = venue + equipment + catering + transport + certificate


registration_income = participants * fee


total_income = registration_income + sponsorship


shortfall = max(0, total_cost - sponsorship)


if fee > 0:
    minimum = math.ceil(shortfall / fee)
else:
    minimum = 0 if sponsorship >= total_cost else -1

print("\n----- EVENT FINANCIAL REPORT -----")

print("Total Event Cost:", total_cost)
print("Registration Income:", registration_income)
print("Sponsorship Amount:", sponsorship)
print("Total Available Income:", total_income)
print("Sponsorship Shortfall:", max(0, total_cost - sponsorship))

if minimum == -1:
    print("Break-even is not possible with zero registration fee")
else:
    print("Minimum Registrations Required:", minimum)

if total_income >= total_cost:
    print("Result: Event is financially successful")
else:
    print("Result: Event needs more funds")

print("Remaining Amount:", max(0, total_cost - total_income))

