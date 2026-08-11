# Append new data to an existing file

with open("student.txt", "a") as file:
    file.write("Status: Learning Python\n")

print("Data appended successfully.")
