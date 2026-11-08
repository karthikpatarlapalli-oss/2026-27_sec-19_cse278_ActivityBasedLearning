
# University Scholarship Allocation System

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")

    marks = []
    for j in range(5):
        mark = int(input("Enter marks in subject " + str(j + 1) + ": "))
        marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    total = sum(marks)
    aggregate = total / 5

    if (aggregate >= 75 and
        min(marks) >= 40 and
        attendance >= 75 and
        income <= 250000):

        print(name, "is Eligible")
        
        students.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

    else:
        print(name, "is Not Eligible")


students.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        x["income"]
    )
)

print("\n===== SCHOLARSHIP RANKING =====")

if len(students) == 0:
    print("No eligible students found.")
else:
    for rank, student in enumerate(students, start=1):
        print("\nRank:", rank)
        print("Name:", student["name"])
        print("Aggregate:", student["aggregate"], "%")
        print("Attendance:", student["attendance"], "%")
        print("Family Income: Rs.", student["income"])

print("\nProgram Completed")

