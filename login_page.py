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
        background-image: url("https://www.ajhospital.in/storage/files/news/Blog/01.jpg");  
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-color: rgba(255, 255, 255, 0.6);
        background-blend-mode: overlay;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    #add space
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    with st.form(key="login_form"):
        # Title
        st.markdown(
            """
            <div style="text-align: center; color: red;">
                <h1 style="font-size: 50px; color:blue;">Login Here !!</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Email and Password inputs
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        # Submit button inside the form
        col1,col2,col3=st.columns([1,2,1])
        with col1:
            if st.form_submit_button("Login",type='primary'):
                if authenticate_user(email, password):
                    st.success(f"Login successful. Welcome {email}!")
                    st.session_state["logged_in"] = True
                    st.session_state["current_user"] = email

                    navigate_to_page("user_home")
                else:
                    st.error("Invalid email or password.")
        with col3:
            if st.form_submit_button("Create an account?",type='primary'):
                navigate_to_page("signup")
