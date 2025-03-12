def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    try:
        import sys
        if sys.stdin.isatty():
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /): ")
        else:
            print("Error: Input not supported in this environment.")
            return
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            return
        
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()
