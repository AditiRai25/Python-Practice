import os

filename = "student.txt"

if os.path.exists(filename):
    print(f"{filename} exists.")
else:
    print(f"{filename} does not exist.")
