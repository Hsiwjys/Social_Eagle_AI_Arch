import streamlit as st

st.set_page_config(page_title="🔢 Number Comparison", layout="centered")

st.title("🔢 Compare Two Numbers")

# User inputs
num1 = st.text_input("Enter first number:")
num2 = st.text_input("Enter second number:")

# Compare button
if st.button("Compare"):
    try:
        n1 = float(num1)
        n2 = float(num2)

        if n1 > n2:
            st.success(f"✅ {n1} is greater than {n2}")
        elif n1 < n2:
            st.success(f"✅ {n1} is less than {n2}")
        else:
            st.info("✅ Both numbers are equal")
    except ValueError:
        st.error("❌ Please enter valid numeric values.")
