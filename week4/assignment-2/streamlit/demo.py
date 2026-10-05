import streamlit_practice as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Class 8 Practice", layout="wide")

# ============================================================
# PART 1: STREAMLIT PRACTICE
# ============================================================

st.title("Class 8 Practice")
st.header("Part 1: Streamlit")

# ------------------------------------------------------------
# Problem 1: Personal greeting
# ------------------------------------------------------------
# Create a text input asking for the learner's name.
# Add a button called "Greet Me".
# When clicked, display:
# "Welcome, <name>!"
#
# Solution:
name = st.text_input("Enter your name", key="p1_name")

if st.button("Greet Me", key="p1_button"):
    st.success(f"Welcome, {name}!")

# ------------------------------------------------------------
# Problem 2: Sidebar preferences
# ------------------------------------------------------------
# Create a sidebar containing:
# 1. A selectbox for choosing a course.
# 2. A slider for choosing a study hours value from 1 to 10.
# 3. A checkbox called "Show summary".
# Display the selected values when the checkbox is checked.
#
# Solution:
st.sidebar.header("Preferences")

course = st.sidebar.selectbox(
    "Choose a course",
    ["Python", "GenAI", "Data Science"]
)

study_hours = st.sidebar.slider(
    "Study hours",
    min_value=1,
    max_value=10,
    value=2
)

show_summary = st.sidebar.checkbox("Show summary")

if show_summary:
    st.write("Course:", course)
    st.write("Study hours:", study_hours)

# ------------------------------------------------------------
# Problem 3: Student score app
# ------------------------------------------------------------
# Create three number inputs for Python, Pandas and NumPy scores.
# Add a button called "Calculate Average".
# Calculate and display the average.
# If average >= 50, show a success message.
# Otherwise show an error message.
#
# Solution:
st.subheader("Student Score App")

python_score = st.number_input("Python score", 0, 100, 50, key="p3_python")
pandas_score = st.number_input("Pandas score", 0, 100, 50, key="p3_pandas")
numpy_score = st.number_input("NumPy score", 0, 100, 50, key="p3_numpy")

if st.button("Calculate Average", key="p3_button"):
    average = (python_score + pandas_score + numpy_score) / 3

    st.write("Average:", average)

    if average >= 50:
        st.success("Passed")
    else:
        st.error("Needs improvement")

# ------------------------------------------------------------
# Problem 4: File uploader
# ------------------------------------------------------------
# Create a file uploader that accepts CSV files.
# If a file is uploaded:
# 1. Read it using Pandas.
# 2. Display the first five rows.
# 3. Display its number of rows and columns.
#
# Solution:
st.subheader("CSV Viewer")

uploaded_csv = st.file_uploader(
    "Upload a CSV file",
    type=["csv"],
    key="p4_file"
)

if uploaded_csv is not None:
    uploaded_df = pd.read_csv(uploaded_csv)

    st.write("First five rows:")
    st.dataframe(uploaded_df.head())

    st.write("Shape:", uploaded_df.shape)

# ------------------------------------------------------------
# Problem 5: Mini Streamlit dashboard
# ------------------------------------------------------------
# Create three columns.
# Column 1 should show total students.
# Column 2 should show average score.
# Column 3 should show highest score.
#
# Solution:
dashboard_df = pd.DataFrame({
    "student": ["A", "B", "C", "D"],
    "score": [80, 65, 90, 75]
})

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Students", len(dashboard_df))

with col2:
    st.metric("Average", dashboard_df["score"].mean())

with col3:
    st.metric("Highest", dashboard_df["score"].max())