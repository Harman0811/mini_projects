# Project Goal:  
# A terminal-based calculator that performs +, −, ×, ÷ operations on two numbers.
# Get Input from User
# Use if-else to Perform Operations

while True:
    choice = input("Do you want to calculate? (yes/no): ")

    if choice.lower() != "yes":
        print("Goodbye!")
        break

    try:
        # Get input
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        # Perform calculation
        if operator == "+":
            print("Result:", num1 + num2)

        elif operator == "-":
            print("Result:", num1 - num2)

        elif operator == "*":
            print("Result:", num1 * num2)

        elif operator == "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Cannot divide by zero")

        else:
            print("Invalid operator")

    except ValueError:
        print("Error: Please enter valid numbers")
