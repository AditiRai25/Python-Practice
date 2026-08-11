# Execute else when no exception occurs

try:
    number = int(input("Enter a number: "))
    result = number * 2

except ValueError:
    print("Error: Invalid input.")

else:
    print("Calculation successful.")
    print("Result:", result)
