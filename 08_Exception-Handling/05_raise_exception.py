# Raise a custom exception when a condition is not satisfied

age = int(input("Enter your age: "))

try:
    if age < 18:
        raise ValueError("Age must be 18 or above.")

    print("Age is valid.")

except ValueError as error:
    print("Error:", error)
