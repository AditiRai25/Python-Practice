# Handle a basic exception using try-except

try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except ValueError:
    print("Error: Please enter a valid number.")
