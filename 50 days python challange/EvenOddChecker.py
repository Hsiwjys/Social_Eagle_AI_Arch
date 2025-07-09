# EvenOddChecker.py

def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

def main():
    try:
        print("Even or Odd Checker")
        print("\nNow checking a list of numbers:")
        numbers = list(map(int, input("Enter numbers separated by space: ").split()))
        for n in numbers:
            print(f"{n} → {check_even_odd(n)}")
    except ValueError:
        print("❌ Error: Please enter valid integers.")

main()
