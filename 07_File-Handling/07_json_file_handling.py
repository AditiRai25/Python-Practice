import json

student = {
    "name": "Aditi",
    "course": "B.Sc IT",
    "skills": ["Python", "SQL", "Java"]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully.")
