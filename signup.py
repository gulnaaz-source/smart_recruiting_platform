import streamlit as st
import sqlite3 as sqlite


col1, col2 = st.columns(2)


remember, forgotpassword = st.columns(2)



with col1:
    st.header("HEXAWARE")
    st.write("Log In to your account")
    st.write("To continue when you left off, please enter your details")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password")
    if st.button("Signup",use_container_width = True, type = "primary"):
        if name == "" and email == "" and password == "":
            st.write("please fill")
        else:
            try:
                connection = sqlite.connect("data.db")
                cursor = connection.cursor()
                acctype = "employee"
                
                cursor.execute("INSERT INTO users (username, email, password, accounttype) VALUES (?, ?, ?, ?)", (name, email, password, acctype))
                connection.commit()
                st.write("Signup successful!")    
                cursor.close()
                connection.close()
            except Exception as e:
                st.write(f"An error occurred: {e}")

    st.checkbox("Remember Me")
    st.page_link("login.py",label = "Already have an account")
            


with col2:
    st.image("login.png")
  
