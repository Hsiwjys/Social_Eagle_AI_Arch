import streamlit as st

st.set_page_config(page_title="Age Category Checker", layout="centered")

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

st.title("👶👦🧔👵 Age Category Checker")

# Input field
age_input = st.text_input("Enter your age:")

if st.button("Check Category"):
    if age_input:
        try:
            age = int(age_input)
            category = age_category(age)
            if category == "Invalid age":
                st.warning("⚠️ Please enter a valid positive age.")
            else:
                st.success(f"✅ Age category: **{category}**")
        except ValueError:
            st.error("❌ Please enter a valid number.")
    else:
        st.info("ℹ️ Please enter your age above.")
