# BasicCalculator.py

def calculator():
    print("Basic Calculator (+, -, *, /)")
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("❌ Error: Cannot divide by zero.")
                return
        else:
            print("❌ Invalid operator.")
            return

        print(f"✅ Result: {result}")
    except ValueError:
        print("❌ Error: Please enter valid numbers.")

calculator()
