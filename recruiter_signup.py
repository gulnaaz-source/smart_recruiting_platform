import streamlit as st

# Create two columns
col1, col2 = st.columns(2)

# Create two sub-columns for "Remember Me" and "Forgot Password"
remember, forgotpassword = st.columns(2)



# Use the first column
with col1:
    st.header("HEXAWARE")
    st.write("Sign Up")
    st.write("Let's get you all st up so you can access your personal account.")
    st.text_input("Full Name")
    st.text_input("Email")
    st.text_input("Organization Name")
    st.text_input("Password")
    st.button("Login",use_container_width = True,type = "primary")
    st.checkbox("I agree to all the terms and  Privacy Policies")
    st.page_link("login.py",label = "Already have an account")

    

# Use the second column
with col2:
    st.image("login.png")
    # Add more widgets here
