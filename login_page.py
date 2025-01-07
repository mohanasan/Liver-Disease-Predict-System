import streamlit as st
from database import authenticate_user
def navigate_to_page(page_name):
    st.session_state["current_page"] = page_name
    st.experimental_rerun()

def login_page():
    # Center the login form using Streamlit form layout
    st.markdown(
    """
    <style>
    /* Apply background image to the main content area */
    .main {
        background-image: url("https://images.rawpixel.com/image_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDI0LTExL3Jhd3BpeGVsb2ZmaWNlNF93aGl0ZV9hbmRfc2lsdmVyX3NpbXBsZV9wbGFpbl9ncmFkaWVudF9iYWNrZ3JvdV8xMTgwZTY5Yy0yNjczLTQ2MTItYmFhNC1jMGFiMDFiODRmYzIuanBn.jpg");  
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    with st.form(key="login_form"):
        # Title
        st.title("Login Page")

        # Email and Password inputs
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        # Submit button inside the form
        col1,col2,col3=st.columns([1,2,1])
        with col1:
            if st.form_submit_button("Login"):
                if authenticate_user(email, password):
                    st.success(f"Login successful. Welcome {email}!")
                    st.session_state["logged_in"] = True
                    st.session_state["current_user"] = email

                    navigate_to_page("user_home")
                else:
                    st.error("Invalid email or password.")
        with col3:
            if st.form_submit_button("Create an account?"):
                navigate_to_page("signup")