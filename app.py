import streamlit as st
import pandas as pd

# --- Load Excel File ---
@st.cache_data
def load_data():
    return pd.read_excel("number_system_questions.xlsx")

df = load_data()

# --- App Title ---
st.title("📘 StepSmart AI - CAT Question Generator (Prototype)")
st.markdown("Generate 20 CAT-style questions from the topic **Number System** based on your preparation level.")

# --- User Input: Exam Selection ---
exam = st.selectbox("Select the exam you're preparing for:", ["CAT", "IPMAT", "XAT", "SNAP"])

# --- User Input: Difficulty ---
difficulty = st.radio("Select difficulty level:", ["Easy", "Medium", "Hard"])

# --- User Input: Topic Coverage ---
coverage = st.slider("How much of Number System have you covered? (%)", 0, 100, 50)

# --- Generate Questions ---
if st.button("🎯 Generate 20 Questions"):
    # Filter questions based on user input
    filtered_df = df[
        (df["Topic"].str.lower() == "number system") &
        (df["Difficulty Level"].str.lower() == difficulty.lower())
    ]
    
    if len(filtered_df) == 0:
        st.warning("No questions available for the selected difficulty.")
    else:
        # Limit to 20 questions or all available
        selected = filtered_df.sample(n=min(20, len(filtered_df)))

        st.success(f"Showing {len(selected)} questions based on your input.")

        # Display each question
        for i, row in selected.iterrows():
            st.markdown(f"**Q{i+1}.** {row['Question']}")
            st.markdown(f"{row['Option']}")
            st.markdown("---")
