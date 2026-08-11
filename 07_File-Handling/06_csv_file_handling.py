import csv

students = [
    ["Name", "Course", "Marks"],
    ["Aditi", "B.Sc IT", 92],
    ["Rahul", "B.Sc IT", 88],
    ["Priya", "B.Sc IT", 95]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created successfully.")
