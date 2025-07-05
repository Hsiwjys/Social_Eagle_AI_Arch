import streamlit as st
import datetime

# Page Configuration
st.set_page_config(page_title="To-Do List 📝", page_icon="✅", layout="centered")

# CSS Styling
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 2.5em;
        margin-bottom: 20px;
    }
    .todo-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        max-width: 700px;
        margin: auto;
    }
    .task-item {
        font-size: 1.1em;
        padding: 5px 0;
    }
    .badge {
        display: inline-block;
        padding: 2px 8px;
        font-size: 0.8em;
        font-weight: bold;
        border-radius: 8px;
        margin-left: 10px;
    }
    .High {
        background-color: #ff4d4d;
        color: white;
    }
    .Medium {
        background-color: #ffa500;
        color: white;
    }
    .Low {
        background-color: #00b894;
        color: white;
    }
    .date {
        font-size: 0.85em;
        color: #555;
        margin-left: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<div class='title'>📝 To-Do List</div>", unsafe_allow_html=True)

# Session State Initialization
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# --- Add Task Form ---
with st.form("add_task", clear_on_submit=True):
    st.subheader("Add a new task ✍️")
    new_task = st.text_input("Task input", placeholder="e.g. Complete assignment", label_visibility="collapsed")
    priority = st.selectbox("Priority", ["High", "Medium", "Low"])
    due_date = st.date_input("Due Date", min_value=datetime.date.today())

    submitted = st.form_submit_button("Add Task")
    if submitted and new_task.strip():
        st.session_state.tasks.append({
            "task": new_task,
            "done": False,
            "priority": priority,
            "due": due_date.strftime("%Y-%m-%d")  # Store date as string
        })

# --- Display Tasks ---
if st.session_state.tasks:
    st.markdown("<div class='todo-box'>", unsafe_allow_html=True)
    st.subheader("Your Tasks:")
    
    for i, t in enumerate(st.session_state.tasks):
        cols = st.columns([0.1, 0.75, 0.15])
        
        # Checkbox
        done = cols[0].checkbox(
            label=f"task_done_{i}",
            value=t["done"],
            key=f"done_{i}",
            label_visibility="collapsed"
        )
        st.session_state.tasks[i]["done"] = done
        
        # Task display
        task_text = f"✅ ~~{t['task']}~~" if done else t['task']
        badge = f"<span class='badge {t['priority']}'>{t['priority']}</span>"
        due = f"<span class='date'>📅 {t['due']}</span>"
        cols[1].markdown(f"<div class='task-item'>{task_text} {badge} {due}</div>", unsafe_allow_html=True)

        # Delete button
        if cols[2].button("🗑️", key=f"delete_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info("No tasks yet! Add one above.")
