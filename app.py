import streamlit as st
from prompt_engine import run_prompt

# Creating a streamlit page
st.set_page_config(page_title="Prompt Engineering App", layout="centered")
st.title("Prompt Engineering App")

# Define prompt types
prompt_types = [
    "Zero-Shot",
    "Few-Shot",
    "Instruction-Based",
    "Chain-of-Thought",
    "Role-Based"
]

# UI for prompt type selection and text input
selected_prompt = st.selectbox("Choose Prompt Type:", prompt_types)
user_input = st.text_area("Enter your prompt here:", height=150)

# Generate content button
if st.button("Generate the Content"):
    with st.spinner("Generating Content..."):
        output = run_prompt(selected_prompt, user_input)
        st.markdown("**Response:**")
        st.code(output)
