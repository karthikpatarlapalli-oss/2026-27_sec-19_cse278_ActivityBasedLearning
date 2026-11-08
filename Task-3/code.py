
# Hospital Billing and Patient Classification System

print("===== HOSPITAL BILLING SYSTEM =====")

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

consultation = float(input("Enter consultation charges: Rs. "))
diagnostic = float(input("Enter diagnostic charges: Rs. "))
treatment = float(input("Enter treatment charges: Rs. "))

student = input("Is patient a student? (yes/no): ").lower()


if age <= 0 or consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid Patient Details or Charges!")

else:

    
    total = consultation + diagnostic + treatment

    
    if age >= 60:
        concession = total * 0.10
        category = "Senior Citizen"

    elif student == "yes":
        concession = total * 0.05
        category = "Student"

    else:
        concession = 0
        category = "General Patient"

    
    final_bill = total - concession

    
    if final_bill < 1000:
        classification = "Low Bill"

    elif final_bill <= 5000:
        classification = "Medium Bill"

    else:
        classification = "High Bill"

    
    print("\n===== PATIENT BILL DETAILS =====")

    print("Patient Name:", name)
    print("Patient Age:", age)
    print("Patient Category:", category)

    print("Consultation Charges: Rs.", consultation)
    print("Diagnostic Charges: Rs.", diagnostic)
    print("Treatment Charges: Rs.", treatment)

    print("Total Bill: Rs.", total)
    print("Concession: Rs.", concession)
    print("Final Payable Amount: Rs.", final_bill)

    print("Patient Classification:", classification)

    print("\nBilling Completed Successfully!")

