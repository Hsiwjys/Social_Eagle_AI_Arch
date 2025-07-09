# SimplePassword.py

def check_password():
    password = input("Enter your password: ")
    min_length = 8

    if len(password) >= min_length:
        print("✅ Password is valid.")
    else:
        print(f"❌ Password too short. Minimum length is {min_length} characters.")

check_password()
