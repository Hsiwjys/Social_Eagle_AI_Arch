
import streamlit as st

# Import your app modules
from apps import (
    AgeCategory, BasicCalculator, CountNumbers, EvenOddChecker,
    NameList, NumberComparison, PersonalGreeting,
    ShoppingBill, SimplePassword, SumCalculator
)

# Mapping app names to modules
app_dict = {
    "🧓 Age Category": AgeCategory,
    "🧮 Basic Calculator": BasicCalculator,
    "🔢 Count Numbers": CountNumbers,
    "➕ Even/Odd Checker": EvenOddChecker,
    "📋 Name List": NameList,
    "🔍 Number Comparison": NumberComparison,
    "👋 Personal Greeting": PersonalGreeting,
    "🛒 Shopping Bill": ShoppingBill,
    "🔐 Simple Password": SimplePassword,
    "➗ Sum Calculator": SumCalculator
}

# Set page config
st.set_page_config(page_title="🏠 50 Days Python Challenge", layout="wide")

# Initialize session state
if "selected_app" not in st.session_state:
    st.session_state.selected_app = list(app_dict.keys())[0]

# Custom CSS for buttons
st.markdown("""
    <style>
    .nav-button {
        background-color: #2e2f38;
        color: white;
        padding: 0.6rem 1rem;
        margin: 0.3rem 0;
        border: none;
        border-radius: 8px;
        width: 100%;
        text-align: left;
        font-size: 1rem;
        font-weight: 500;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    .nav-button:hover {
        background-color: #444654;
    }
    .nav-button-active {
        background-color: #ff4b4b !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation with plain buttons (no radio/selectbox)
with st.sidebar:
    st.title("📚 App Navigation")
    st.markdown('<h4>📱⬇️ <b>Choose an app to run</b></h4>', unsafe_allow_html=True)
    for app_name in app_dict.keys():
        button_class = "nav-button"
        if st.session_state.selected_app == app_name:
            button_class += " nav-button-active"
        if st.button(app_name, key=app_name):
            st.session_state.selected_app = app_name

# Main content
st.title("🚀 50 Days Python Challenge")
st.subheader(f"📌 Currently Running: {st.session_state.selected_app}")
st.markdown("---")
app_dict[st.session_state.selected_app].app()
