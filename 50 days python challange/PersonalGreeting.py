import streamlit as st

st.set_page_config(page_title="🛒 Shopping Bill Calculator", layout="centered")

st.title("🛍️ Shopping Bill Calculator")

# Input number of items
num_items = st.number_input("Enter number of items 🧾:", min_value=1, step=1)

# Collect prices
prices = []
for i in range(num_items):
    price = st.number_input(f"Price of item {i + 1} (₹):", min_value=0.0, format="%.2f", key=f"price_{i}")
    prices.append(price)

# Tax input
tax_percent = st.number_input("Enter tax percentage (e.g., 5 for 5%):", min_value=0.0, format="%.2f")

# Calculate button
if st.button("Calculate Total"):
    subtotal = sum(prices)
    tax_amount = (tax_percent / 100) * subtotal
    total = subtotal + tax_amount

    st.success(f"🛒 Subtotal: ₹{subtotal:.2f}")
    st.info(f"🧾 Tax ({tax_percent}%): ₹{tax_amount:.2f}")
    st.success(f"💰 Total Bill: ₹{total:.2f}")
