# app.py
import streamlit as st
import hashlib
from home import show_home_page
from user_profile import show_profile_page
from inventory import show_inventory_page
from recipes import show_recipes_page
from meal_plan import show_meal_plan_page
from shopping_list import show_shopping_list_page
from community import show_community_page

import yaml

# Load user data from a YAML file (create one if it doesn't exist)
def load_user_data():
    try:
        with open('user_data.yaml', 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        return {}  # Initialize an empty dictionary if the file doesn't exist

# Save user data to the YAML file
def save_user_data(user_data):
    with open('user_data.yaml', 'w') as file:
        yaml.dump(user_data, file)

# Register a new user
def register_user(email, password):
    user_data = load_user_data()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user_data[email] = hashed_password
    save_user_data(user_data)
    st.success(f"Registration successful for {email}!")

# Authenticate user credentials
def authenticate_user(email, password):
    user_data = load_user_data()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if email in user_data and user_data[email] == hashed_password:
        return True
    return False

def show_registration_page():
    st.subheader("Register")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    register_button = st.button("Register")

    if register_button:
        if password == confirm_password:
            register_user(email, password)
        else:
            st.error("Passwords do not match. Please try again.")

def show_login_page():
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    login_button = st.button("Log In")

    if login_button:
        if authenticate_user(email, password):
            st.success("Login successful!")
            return email  # Return user's email as user ID
        else:
            st.error("Invalid email or password. Please try again.")

def main():
    st.title("Pantry Palate")
    st.header("Your Personal Meal Planning Assistant")

    st.sidebar.subheader("Navigation")
    page = st.sidebar.radio("", ["Home", "Profile", "Inventory", "Recipes", "Meal Plan", "Shopping List", "Community", "Login", "Register"])

    if page == "Home":
        user_id = show_login_page()
        if user_id:
            # Implement your home page logic here
            st.write(f"Welcome, {user_id}!")
    elif page == "Register":
        show_registration_page()
    # Add other page handling logic here

if __name__ == "__main__":
    main()

"""
# Mock user database (user_id: password)
user_database = {
    "john@example.com": "password123",
    "emma@example.com": "letmein",
    # Add more users as needed
}

# Function to authenticate user credentials
def authenticate_user(email, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if email in user_database and user_database[email] == hashed_password:
        return True
    return False

# Function to register a new user
def register_user(email, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user_database[email] = hashed_password
    st.success("Registration successful! You can now log in.")

# Function to display the login page
def show_login_page():
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    login_button = st.button("Log In")

    if login_button:
        if authenticate_user(email, password):
            st.success("Login successful!")
            return email  # Return user's email as user ID
        else:
            st.error("Invalid email or password. Please try again.")

# Function to display the registration page
def show_registration_page():
    st.subheader("Register")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    register_button = st.button("Register")

    if register_button:
        if password == confirm_password:
            register_user(email, password)
        else:
            st.error("Passwords do not match. Please try again.")

# Main function to run the Streamlit app
def main():
    st.title("Pantry Palate")
    st.header("Your Personal Meal Planning Assistant")

    st.sidebar.subheader("Navigation")
    page = st.sidebar.radio("", ["Home", "Profile", "Inventory", "Recipes", "Meal Plan", "Shopping List", "Community", "Login", "Register"])

    if page == "Home":
        user_id = show_login_page()
        if user_id:
            show_home_page(user_id)
    elif page == "Profile":
        user_id = show_login_page()
        if user_id:
            show_profile_page(user_id)
    elif page == "Inventory":
        user_id = show_login_page()
        if user_id:
            show_inventory_page(user_id)
    elif page == "Recipes":
        user_id = show_login_page()
        if user_id:
            show_recipes_page(user_id)
    elif page == "Meal Plan":
        user_id = show_login_page()
        if user_id:
            show_meal_plan_page(user_id)
    elif page == "Shopping List":
        user_id = show_login_page()
        if user_id:
            show_shopping_list_page(user_id)
    elif page == "Community":
        user_id = show_login_page()
        if user_id:
            show_community_page(user_id)
    elif page == "Login":
        show_login_page()
    elif page == "Register":
        show_registration_page()
if __name__ == "__main__":
    main()
"""













###############
# import streamlit_authenticator as stauth  # Import Streamlit-Authenticator

# # Load user credentials from the YAML file
# user_credentials = stauth.load_credentials("credentials.yaml")

# # Create an authenticator object
# authenticator = stauth.Authenticator(user_credentials)

# # Function to display the login page
# def show_login_page():
#     st.subheader("Login")
#     if authenticator.login_widget():
#         st.success("Login successful!")
#         return authenticator.get_username()  # Return user's email as user ID

# # Function to display the registration page
# def show_registration_page():
#     st.subheader("Register")
#     try:
#         if authenticator.register_user("Register user", preauthorization=False):
#             st.success("User registered successfully!")
#     except Exception as e:
#         st.error(e)

# # Main function to run the Streamlit app
# def main():
#     st.title("Pantry Palate")
#     st.header("Your Personal Meal Planning Assistant")

#     st.sidebar.subheader("Navigation")
#     page = st.sidebar.radio("", ["Home", "Profile", "Inventory", "Recipes", "Meal Plan", "Shopping List", "Community", "Login", "Register"])

#     if page == "Home":
#         user_id = show_login_page()
#         if user_id:
#             # Implement logic for the Home page
#             pass
#     elif page == "Profile":
#         # Implement logic for the Profile page
#         pass
#     # ... (similarly for other pages)

#     if page == "Home":
#         user_id = show_login_page()
#         if user_id:
#             show_home_page(user_id)
#     elif page == "Profile":
#         user_id = show_login_page()
#         if user_id:
#             show_profile_page(user_id)
#     elif page == "Inventory":
#         user_id = show_login_page()
#         if user_id:
#             show_inventory_page(user_id)
#     elif page == "Recipes":
#         user_id = show_login_page()
#         if user_id:
#             show_recipes_page(user_id)
#     elif page == "Meal Plan":
#         user_id = show_login_page()
#         if user_id:
#             show_meal_plan_page(user_id)
#     elif page == "Shopping List":
#         user_id = show_login_page()
#         if user_id:
#             show_shopping_list_page(user_id)
#     elif page == "Community":
#         user_id = show_login_page()
#         if user_id:
#             show_community_page(user_id)
#     elif page == "Login":
#         show_login_page()
#     elif page == "Register":
#         show_registration_page()

# if __name__ == "__main__":
#     main()


############

# # app.py
# import sqlite3  # Using SQLite for simplicity (you can replace with other databases)

# # Create an SQLite database (or use a cloud-based database)
# conn = sqlite3.connect("user_database.db")
# cursor = conn.cursor()

# # Create a table to store user credentials
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         email TEXT PRIMARY KEY,
#         password TEXT
#     )
# """)
# conn.commit()

# # Function to authenticate user credentials
# def authenticate_user(email, password):
#     hashed_password = hashlib.sha256(password.encode()).hexdigest()
#     cursor.execute("SELECT email FROM users WHERE email = ? AND password = ?", (email, hashed_password))
#     result = cursor.fetchone()
#     return result is not None

# # Function to register a new user
# def register_user(email, password):
#     hashed_password = hashlib.sha256(password.encode()).hexdigest()
#     try:
#         cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed_password))
#         conn.commit()
#         st.success("Registration successful! You can now log in.")
#     except sqlite3.IntegrityError:
#         st.error("User with this email already exists. Please choose a different email.")

# # Function to display the login page
# def show_login_page():
#     st.subheader("Login")
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")
#     login_button = st.button("Log In")

#     if login_button:
#         if authenticate_user(email, password):
#             st.success("Login successful!")
#             return email  # Return user's email as user ID
#         else:
#             st.error("Invalid email or password. Please try again.")

# # Function to display the registration page
# def show_registration_page():
#     st.subheader("Register")
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")
#     confirm_password = st.text_input("Confirm Password", type="password")
#     register_button = st.button("Register")

#     if register_button:
#         if password == confirm_password:
#             register_user(email, password)
#         else:
#             st.error("Passwords do not match. Please try again.")

# # Rest of your code remains unchanged
# # Main function to run the Streamlit app
# def main():
#     st.title("Pantry Palate")
#     st.header("Your Personal Meal Planning Assistant")

#     st.sidebar.subheader("Navigation")
#     page = st.sidebar.radio("", ["Home", "Profile", "Inventory", "Recipes", "Meal Plan", "Shopping List", "Community", "Login", "Register"])

#     if page == "Home":
#         user_id = show_login_page()
#         if user_id:
#             # Implement logic for the Home page
#             pass
#     elif page == "Profile":
#         # Implement logic for the Profile page
#         pass
#     # ... (similarly for other pages)

# if __name__ == "__main__":
#     main()
