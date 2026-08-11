try:
    with open("student.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")
