# ShoppingBill.py

def main():
    try:
        n = int(input("Enter number of items: "))
        total = 0
        for i in range(n):
            price = float(input(f"Enter price of item {i+1}: "))
            total += price

        tax_percent = float(input("Enter tax percentage (e.g., 5 for 5%): "))
        tax_amount = (tax_percent / 100) * total
        grand_total = total + tax_amount

        print(f"\n🛒 Subtotal: ₹{total:.2f}")
        print(f"🧾 Tax: ₹{tax_amount:.2f}")
        print(f"💰 Total Bill: ₹{grand_total:.2f}")
    except ValueError:
        print("❌ Error: Please enter valid numeric values.")

main()
