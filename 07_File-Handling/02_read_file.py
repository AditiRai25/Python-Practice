# Read data from a file

with open("student.txt", "r") as file:
    data = file.read()

print("File Content:")
print(data)
