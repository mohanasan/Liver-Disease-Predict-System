import streamlit as st
from streamlit_option_menu import option_menu
from database import fetch_user
import base64
import pandas as pd
def navigate_to_page(page_name):
    st.session_state["current_page"] = page_name
    st.experimental_rerun()

def user_home_page():
    user = fetch_user(st.session_state["current_user"])
    with st.sidebar:
        select = option_menu(
            f"Welcome, {user[1]}!",
            ["User Profile",'Prediction','Nearby Doctors', "Feedback","Logout"],
            icons=['person-vcard-fill','cloud-upload','plus-lg','hand-thumbs-up' ,'unlock-fill'],
            menu_icon="cast",
            default_index=0,
            orientation="vertical",
        )

    if select == 'User Profile':
        st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url('https://media.istockphoto.com/id/958522248/photo/the-concept-of-a-healthy-liver.jpg?s=612x612&w=0&k=20&c=WVarRCQ7LXNTGAWT0ItAsYD8oCjFoCIwHKRbsuJLP98=');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        </style>
        """,
        unsafe_allow_html=True
        )

        # Extracting user data from session state after successful login
        if user:
            # Assuming 'user' is a tuple (id, name, email, password, regd_no, year_of_study, branch, student_type, student_image)
            name, age, gender = user[1], user[3], user[4]
            if gender == 'Male':
                image_link = "https://cdn-icons-png.freepik.com/256/3135/3135768.png?semt=ais_hybrid"
            else:
                image_link = "https://cdn-icons-png.flaticon.com/512/219/219969.png"

            # CSS Styling for vertical container
            profile_css = """
            <style>
                .profile-container {
                    background-color: #a3ebff;
                    padding: 50px;
                    border-radius: 20px;
                    box-shadow: 10px 8px 12px rgba(0, 0, 0, 0.15);
                    max-width: 300px;
                    border: 2px solid black;
                    margin-left: 100%;
                    margin: auto;
                    font-family: Arial, sans-serif;
                    text-align: center;
                }
                .profile-header {
                    font-size: 24px;
                    font-weight: bold;
                    margin-bottom: 15px;
                    color: #333;
                }
                .profile-item {
                    font-size: 18px;
                    margin-bottom: 10px;
                    color: #555;
                }
                .profile-image img {
                    border-radius: 50%;
                    max-width: 200px;
                    max-height: 200px;
                    margin-bottom: 20px;
                }
            </style>
            """

            # HTML Structure for vertical alignment
            profile_html = f"""
            <div class="profile-container">
                <div class="profile-image">
                    <img src="{image_link}" alt="User Image">
                </div>
                <div class="profile-details">
                    <div class="profile-header">User Report</div>
                    <div class="profile-item"><strong>Name:</strong> {name}</div>
                    <div class="profile-item"><strong>Age:</strong> {age}</div>
                    <div class="profile-item"><strong>Gender:</strong> {gender}</div>
                </div>
            </div>
            """

            # Display styled content
            st.markdown(profile_css + profile_html, unsafe_allow_html=True)
    elif select == 'Nearby Doctors':
        st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url("https://www.shutterstock.com/image-photo/medical-worker-plus-icon-represents-600nw-2474393153.jpg");  
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        </style>
        """,
        unsafe_allow_html=True
        )

        # Load data
        data = pd.read_csv('doctors.csv', encoding='utf-8', on_bad_lines='skip')

        # Select doctor region
        names = st.selectbox('Select Doctor Name', data['Region'].unique())
        df = pd.DataFrame(data[data['Region'] == names])
        # Extract doctor and hospital information
        d1, d2, d3, d4, d5 = df['Doctor Name'][:5]
        h1, h2, h3, h4, h5 = df['Hospital Name'][:5]
        region = names
        i1 = "https://img.pikbest.com/origin/10/06/86/45ZpIkbEsTKq4.png!sw800"
        i2="https://static.vecteezy.com/system/resources/previews/041/642/113/non_2x/ai-generated-portrait-of-young-doctor-man-happy-smiling-free-png.png"
        i3="https://png.pngtree.com/png-clipart/20230918/ourmid/pngtree-photo-men-doctor-physician-chest-smiling-png-image_10132895.png"
        i4="https://static.vecteezy.com/system/resources/thumbnails/041/408/858/small_2x/ai-generated-a-smiling-doctor-with-glasses-and-a-white-lab-coat-isolated-on-transparent-background-free-png.png"
        i5="https://pngimg.com/d/doctor_PNG15992.png"
        profile_css = """
            <style>
                .profile-container {
                    background-color: #adf23d;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                    max-width: 300px;
                    border: 1px solid #ccc;
                    margin: 10px;
                    font-family: Arial, sans-serif;
                    text-align: center;
                }
                .profile-header {
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 10px;
                    color: #333;
                }
                .profile-item {
                    font-size: 14px;
                    margin-bottom: 5px;
                    color: #555;
                }
                .profile-image img {
                    border-radius: 50%;
                    max-width: 100px;
                    max-height: 100px;
                    margin-bottom: 10px;
                }
            </style>
        """

        # HTML template
        def create_profile_html(name, hospital, region, image_link):
            return f"""
            <div class="profile-container">
                <div class="profile-image">
                    <img src="{image_link}" alt="User Image">
                </div>
                <div class="profile-details">
                    <div class="profile-header">User Report</div>
                    <div class="profile-item"><strong>Name:</strong> {name}</div>
                    <div class="profile-item"><strong>Region:</strong> {region}</div>
                    <div class="profile-item"><strong>Hospital:</strong> {hospital}</div>
                </div>
            </div>
            """

        # Display 3 profiles in 3 columns
        col1, col2, col3 = st.columns(3)
        col1.markdown(profile_css + create_profile_html(d1, h1, region,i1), unsafe_allow_html=True)
        col2.markdown(profile_css + create_profile_html(d2, h2, region,i2), unsafe_allow_html=True)
        col3.markdown(profile_css + create_profile_html(d3, h3, region,i3), unsafe_allow_html=True)
        
        # Display 2 profiles in 2 columns
        col4, col5 = st.columns(2)
        col4.markdown(profile_css + create_profile_html(d4, h4, region,i4), unsafe_allow_html=True)
        col5.markdown(profile_css + create_profile_html(d5, h5, region,i5), unsafe_allow_html=True)

    elif select == 'Feedback':
        st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url("https://img.freepik.com/free-psd/3d-emoji-frame-isolated_23-2151171338.jpg?semt=ais_hybrid");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        </style>
        """,
        unsafe_allow_html=True
        )
        with st.form('About Us'):
            # Contact Us Form
            st.subheader(f"Hello {user[1]} Fill Feedback!! ✍️")

            # Create form fields
            name = user[1]
            email = user[2]
            phone = st.text_input("Phone Number")
            issue = st.text_area("Describe your Feedback!!")

            # Submit button
            if st.form_submit_button("Submit"):
                if issue and phone:
                    # Process the form data (you can save it or send an email here)
                    st.success("Thank you for reaching out! We'll get back to you soon.")
                else:
                    st.error("Please fill in all fields before submitting.")
    elif select == 'Prediction':
        st.markdown(
            """
            <style>
            /* Apply background image to the main content area */
            .main {
                background-color: #a5e7fa;
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        info = pd.read_csv('./dataset.csv')
        info['Albumin_and_Globulin_Ratio'].fillna(info['Albumin_and_Globulin_Ratio'].median(),inplace=True)
        # info.isna().sum() 
        from sklearn import tree
        from sklearn.model_selection import train_test_split

        # info.info() # info

        dt = tree.DecisionTreeClassifier()
        #  rename 
        info.rename(columns ={'Dataset':'Target'},inplace=True)


        # # In[81]:


        X = info.drop('Target',axis=1)
        y = info['Target']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        dt.fit(X_train,y_train)
        col1,col2,col3 = st.columns([1,8,1])
        col2.title("Liver Disease Prediction")
        with st.form('Prediction'):
            col1,col2 = st.columns(2)
            sex=col1.selectbox('Select Gender', ['Male','Female'])
            if sex=='Male':
                Sex=1
            else:
                Sex=2
            age = col2.slider('Select Age', 0, 100, 25) 
            col1,col2 = st.columns(2)
            Total_Bilirubin = col1.number_input("Enter your Total_Bilirubin") # 3
            Direct_Bilirubin = col2.number_input("Enter your Direct_Bilirubin")# 4
            Alkaline_Phosphotase = col1.number_input("Enter your Alkaline_Phosphotase") # 5
            Alamine_Aminotransferase = col2.number_input("Enter your Alamine_Aminotransferase") # 6
            Aspartate_Aminotransferase = col1.number_input("Enter your Aspartate_Aminotransferase") # 7
            Total_Protiens = col2.number_input("Enter your Total_Protiens")# 8
            Albumin = col1.number_input("Enter your Albumin") # 9
            Albumin_and_Globulin_Rati = col2.number_input("Enter your Albumin_and_Globulin_Ratio") # 10 

            if st.form_submit_button('Submit',type='primary'):
                results = dt.predict([[Sex,age,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase
                                ,Total_Protiens,Albumin,Albumin_and_Globulin_Rati]])
                
                for final in results:
                    if final == 1:
                        st.error(f'{user[1]} you have a Liver Disease')
                    else:
                        st.success(f'{user[1]} you are Healthy')

    elif select == 'Logout':
        st.session_state["logged_in"] = False
        st.session_state["current_user"] = None
        navigate_to_page("home")
