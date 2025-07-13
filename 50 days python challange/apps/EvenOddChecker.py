import streamlit as st

def app():
    st.set_page_config(page_title="🔍 Even or Odd Checker", layout="centered")

    def check_even_odd(number):
        return "Even" if number % 2 == 0 else "Odd"

    st.title("🔢 Even or Odd Checker")

    # Input from user
    user_input = st.text_input("Enter numbers separated by space (e.g., 5 10 3 8):")

    if st.button("Check"):
        if user_input:
            try:
                numbers = list(map(int, user_input.strip().split()))
                st.success("✅ Results:")
                for n in numbers:
                    result = check_even_odd(n)
                    st.write(f"🔹 {n} → **{result}**")
            except ValueError:
                st.error("❌ Error: Please enter valid integers only.")
        else:
            st.info("ℹ️ Please enter some numbers above.")
