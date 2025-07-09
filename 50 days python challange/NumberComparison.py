# NumberComparison.py

def compare_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if num1 > num2:
            print(f"✅ {num1} is greater than {num2}")
        elif num1 < num2:
            print(f"✅ {num1} is less than {num2}")
        else:
            print("✅ Both numbers are equal")
    except ValueError:
        print("❌ Please enter valid numbers.")

compare_numbers()
