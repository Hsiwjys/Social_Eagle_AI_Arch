import streamlit as st

st.set_page_config(page_title="🧮 Basic Calculator", layout="centered")

st.title("🧮 Basic Calculator")

# Input fields
num1 = st.text_input("Enter first number:")
operator = st.selectbox("Choose operator", ['+', '-', '*', '/'])
num2 = st.text_input("Enter second number:")

# Button to calculate
if st.button("Calculate"):
    try:
        n1 = float(num1)
        n2 = float(num2)

        # Perform calculation
        if operator == '+':
            result = n1 + n2
        elif operator == '-':
            result = n1 - n2
        elif operator == '*':
            result = n1 * n2
        elif operator == '/':
            if n2 != 0:
                result = n1 / n2
            else:
                st.error("❌ Error: Cannot divide by zero.")
                result = None
        else:
            st.error("❌ Invalid operator.")
            result = None

        if result is not None:
            st.success(f"✅ Result: **{result}**")
    except ValueError:
        st.error("❌ Please enter valid numbers.")
