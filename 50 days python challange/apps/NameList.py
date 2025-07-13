import streamlit as st

def app():
    st.set_page_config(page_title="📋 Name List", layout="centered")

    # Title of the app
    st.title("📋 Name List with Lengths")

    # Number of names to enter
    n = st.number_input("Enter number of names:", min_value=1, step=1)

    # Input fields for each name
    names = []
    for i in range(n):
        name = st.text_input(f"Enter name {i+1}:", key=f"name_{i}")
        if name:
            names.append(name)

    # Button to show names with lengths
    if st.button("Show Name Lengths"):
        if names:
            st.subheader("📝 Names and Their Lengths:")
            for name in names:
                st.write(f"🔹 {name} → {len(name)} characters")
        else:
            st.warning("Please enter at least one name.")
