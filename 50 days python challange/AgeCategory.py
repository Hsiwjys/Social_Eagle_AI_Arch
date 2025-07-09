# AgeCategory.py

def age_category(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

def main():
    try:
        age = int(input("Enter age: "))
        category = age_category(age)
        print(f"✅ Age category: {category}")
    except ValueError:
        print("❌ Error: Please enter a valid number.")

main()
