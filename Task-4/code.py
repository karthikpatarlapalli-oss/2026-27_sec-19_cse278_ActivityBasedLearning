
# Employee Payroll and Deduction Analysis

print("===== EMPLOYEE PAYROLL SYSTEM =====")

name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

basic = float(input("Enter basic pay: Rs. "))
hours = float(input("Enter overtime hours: "))
incentive = float(input("Enter incentive amount: Rs. "))


if basic < 0 or hours < 0 or incentive < 0:
    print("Invalid Salary Details!")

else:
    
    hra = basic * 0.20
    da = basic * 0.10

    
    overtime = hours * 150

    
    gross = basic + hra + da + overtime + incentive

    
    if gross <= 10000:
        deduction = 0

    elif gross <= 20000:
        deduction = (gross - 10000) * 0.05

    elif gross <= 30000:
        deduction = (10000 * 0.05) + (gross - 20000) * 0.10

    else:
        deduction = (10000 * 0.05) + (10000 * 0.10) + (gross - 30000) * 0.15

    
    net = gross - deduction

    
    print("\n===== SALARY STATEMENT =====")

    print("Employee Name:", name)
    print("Employee ID:", emp_id)

    print("----------------------------")
    print("Basic Pay: Rs.", basic)
    print("HRA: Rs.", hra)
    print("DA: Rs.", da)
    print("Overtime: Rs.", overtime)
    print("Incentives: Rs.", incentive)

    print("----------------------------")
    print("Gross Salary: Rs.", gross)
    print("Total Deduction: Rs.", round(deduction, 2))
    print("Net Salary: Rs.", round(net, 2))

    print("----------------------------")
    print("Payroll Completed Successfully!")

