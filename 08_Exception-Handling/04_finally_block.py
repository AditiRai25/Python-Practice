# The finally block always executes

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)

except (ValueError, ZeroDivisionError):
    print("Error: Invalid input or division by zero.")

finally:
    print("Program execution completed.")
