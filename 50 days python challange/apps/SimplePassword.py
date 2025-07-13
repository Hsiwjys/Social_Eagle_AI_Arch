import streamlit as st
import re

def app():
    st.set_page_config(page_title="🔐 Password Strength Checker", layout="centered")
    st.title("🔐 Password Strength Checker")

    # Password input
    password = st.text_input("Enter your password:", type="password")

    def check_strength(pwd):
        strength = 0
        remarks = []

        if len(pwd) >= 8:
            strength += 1
        else:
            remarks.append("Less than 8 characters")

        if re.search(r"[a-z]", pwd):
            strength += 1
        else:
            remarks.append("No lowercase letter")

        if re.search(r"[A-Z]", pwd):
            strength += 1
        else:
            remarks.append("No uppercase letter")

        if re.search(r"\d", pwd):
            strength += 1
        else:
            remarks.append("No number")

        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
            strength += 1
        else:
            remarks.append("No special character")

        if strength <= 2:
            return "❌ Weak", remarks
        elif strength == 3 or strength == 4:
            return "⚠️ Medium", remarks
        else:
            return "✅ Strong", []

    # Strength Check
    if password:
        strength_level, issues = check_strength(password)
        st.subheader(f"Password Strength: {strength_level}")
        if issues:
            with st.expander("Suggestions to Improve"):
                for issue in issues:
                    st.write(f"• {issue}")
