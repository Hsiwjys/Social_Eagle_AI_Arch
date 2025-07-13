import streamlit as st

def app():
    st.set_page_config(page_title="🎨 Personalized Message Generator", layout="centered")

    st.title("🌟 Personalized Message Generator")

    # Input fields
    name = st.text_input("Enter your Name 🧑‍💻:")
    age = st.number_input("Enter your age 🎂:", min_value=0, step=1)
    fav_color = st.text_input("Enter your favorite color 🎨:")

    # Generate button
    if st.button("Generate Message"):
        if name and fav_color:
            message = f"""
            🌟 Meet **{name.upper()}**! 🌟

            At **{age}** years young, you're painting the world with your love for **{fav_color.title()}** 🎨✨  
            That's not just a color — it's your vibe, your energy, your signature! 💫

            Keep shining, dreaming, and coloring the world your way! 🚀🌈
            """
            st.success(message)
        else:
            st.warning("⚠️ Please fill in all the fields to get your personalized message.")
