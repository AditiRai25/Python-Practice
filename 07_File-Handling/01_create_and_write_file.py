# Create a file and write data into it

with open("student.txt", "w") as file:
    file.write("Name: Aditi\n")
    file.write("Course: B.Sc IT\n")
    file.write("Subject: Python\n")

print("Data written successfully.")
