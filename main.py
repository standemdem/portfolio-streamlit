import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# Page 1: Introduction
def introduction_page():
    st.title("Welcome to Stanislas's Portfolio")
    st.write("Hello, I'm Stanislas, an IVVQ engineer looking for new opportunities.")
    st.write("I specialize in Integration, Validation, Verification, and Qualification (IVVQ).")
    st.write("I am passionate about ensuring the quality and reliability of complex systems.")
    st.write("My unique combination of skills and experience makes me a valuable asset in the field.")

# Page 2: Projects Summary (Details will be added later)
def projects_summary_page():
    st.title("Projects Summary")
    st.write("This page will contain a summary of the different projects I have worked on.")

# Sidebar navigation
page_options = {
    "Introduction": introduction_page,
    "Projects Summary": projects_summary_page,
}

selected_page = st.sidebar.radio("Select a page", list(page_options.keys()))

# Display the selected page
page_options[selected_page]()
