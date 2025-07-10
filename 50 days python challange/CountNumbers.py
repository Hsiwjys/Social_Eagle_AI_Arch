import streamlit as st

st.set_page_config(page_title="Count Numbers", layout="centered")

st.title("🔢 Count Positive, Negative & Zero Numbers")

# User input
user_input = st.text_input("Enter a list of numbers separated by commas (e.g., 5, -2, 0, 9, -1):")

if st.button("🔍 Analyze"):
    try:
        # Convert input string to list of numbers
        number_list = [int(num.strip()) for num in user_input.split(",") if num.strip()]

        # Counters
        positive = sum(1 for n in number_list if n > 0)
        negative = sum(1 for n in number_list if n < 0)
        zeros = sum(1 for n in number_list if n == 0)

        # Display results
        st.success("✅ Results:")
        st.write(f"🔹 Positive Numbers: `{positive}`")
        st.write(f"🔸 Negative Numbers: `{negative}`")
        st.write(f"⚪ Zeroes: `{zeros}`")

    except ValueError:
        st.error("❌ Please enter only integers separated by commas.")
