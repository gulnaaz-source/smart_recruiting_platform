import streamlit as st
import sqlite3 as sqlite

# Set the page configuration with a custom title and icon
st.set_page_config(page_title="HEXAWARE Login", page_icon=":key:", layout="wide")

# Define the HEX color code for the logo color
logo_color = "#0056b3"  # This is a shade of blue matching the logo

# Add custom CSS for a more polished look
st.markdown(f"""
    <style>
        .main {{
            background-color: #f0f2f6;
            padding: 20px;
        }}
        .stButton > button {{
            background-color: #007bff;
            color: white;
            border-radius: 5px;
            border: none;
            padding: 10px;
        }}
        .stButton > button:hover {{
            background-color: #0056b3;
        }}
        .stTextInput > div > input {{
            border-radius: 5px;
            border: 1px solid #ccc;
            padding: 10px;
            font-size: 16px;
        }}
        .stCheckbox > div > div > label {{
            font-size: 14px;
        }}
        .custom-header {{
            color: {logo_color};
            font-size: 32px;
            font-weight: bold;
        }}
    </style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
remember, forgotpassword = st.columns(2)

def Forgotpassword():
    st.header("Forgot Password")
    st.write("Enter the email or phone number associated with your account and we'll email you the reset password link.")
    st.text_input("Email/Username")
    st.button("Submit", use_container_width=True, type="primary")

with col1:
    # Display the header with the specific logo color
    st.markdown(f"<h1 class='custom-header'>HEXAWARE</h1>", unsafe_allow_html=True)
    st.subheader("Log In to your account")
    st.write("To continue where you left off, please enter your details.")
    
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")  # Mask the password input

    if st.button("Login", use_container_width=True):
        if email == "" or password == "":
            st.warning("Please fill in both fields")
        else:
            try:
                connection = sqlite.connect("data.db")
                cursor = connection.cursor()
                
                cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
                user = cursor.fetchone()
                
                if user:
                    st.success("Login successful!")
                else:
                    st.error("Invalid email or password")
                
                cursor.close()
                connection.close()
            except Exception as e:
                st.error(f"An error occurred: {e}")

    with remember:
        st.checkbox("Remember Me")

    with forgotpassword:
        if st.button("Forgot Password"):
            Forgotpassword()

st.write("[Don't have an account? Sign up](pages/ask.py)")

with col2:
    st.image("login.png", caption="Welcome to HEXAWARE", use_column_width=True)




 