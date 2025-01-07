import streamlit as st
from database import add_user
import re
def navigate_to_page(page_name):
    st.session_state["current_page"] = page_name
    st.experimental_rerun()
def validate_mail(mail):
    valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', mail)
    return True
def signup_page():
    st.markdown(
    """
    <style>
    /* Apply background image to the main content area */
    .main {
        background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReyiG0pG118dpW-JZCkLcrvfKMYo2rdtS-9Q&s");  
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    st.title("Sign Up Here!")
    with st.form(key="signup_form"):
        name=st.text_input("Name")
        email = st.text_input("Email", key="signup_email")
        col1,col2=st.columns([1,1])
        age=col1.slider("Age", 0, 100, 0, 1)
        gender=col2.selectbox("Gender", ["Male","Female","Other"])
        col1,col2=st.columns([1,1])
        password = col1.text_input("Create a Password", type="password", key="signup_password")
        retyped_password = col2.text_input("Retype Password", type="password", key="signup_retyped_password")
        col1,col2,col3 = st.columns([1,1,1])
        with col1:
            if st.form_submit_button("Sign Up") and validate_mail(email)!=None and len(password)>=6 and password==retyped_password and age and gender and name:
                try:
                    add_user(name,email,age,gender,password)
                    st.success("Account created successfully!!")
                    navigate_to_page("login")
                except Exception as e:
                    st.error('Already have an account with this email address. Please login.')
            elif validate_mail(email)==None:
                st.error("Invalid email address. Please enter a valid email address.")
            elif password!=retyped_password:
                st.error("Passwords do not match.")
            elif len(password)<6 and len(password)!=0:
                st.error("Password must be at least 8 characters long.")
        with col3:
            if st.form_submit_button("Already have an account?"):
                navigate_to_page("login")