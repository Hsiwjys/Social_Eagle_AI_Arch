import streamlit as st

def app():
    st.set_page_config(page_title="🧮 Sum Calculator", layout="centered")

    # Title
    st.title("🧮 Sum Calculator")

    # Input from user
    n = st.number_input("Enter a positive integer (n):", min_value=1, step=1)

    # Calculate sum using loop
    def calculate_sum(n):
        total = 0
        for i in range(1, n + 1):
            total += i
        return total

    # Button to trigger calculation
    if st.button("Calculate Sum"):
        result = calculate_sum(n)
        st.success(f"The sum of all numbers from 1 to {n} is: {result}")
