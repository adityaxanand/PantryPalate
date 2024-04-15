import streamlit as st

# Function to save user profile data to a file or database
def save_profile_data(profile_data):
    # Code to save the profile data (mocked for now)
    with open("user_profiles.txt", "a") as file:
        file.write(f"Name: {profile_data['name']}, Age: {profile_data['age']}, Weight: {profile_data['weight']} kg, Height: {profile_data['height']} cm\n")
        file.write(f"Dietary Preferences: {', '.join(profile_data['dietary_preferences'])}\n")
        file.write(f"Nutritional Goals: {profile_data['nutritional_goals']}\n")
    return True

# Function to display the user profile page
def show_profile_page():
    st.subheader("Profile")
    st.write("This is the Profile page.")
    # Add form inputs for user profile creation
    with st.form("user_profile_form"):
        st.write("Please fill out the following details:")
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=150, step=1)
        weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1)
        height = st.number_input("Height (cm)", min_value=0.0, step=0.1)
        dietary_preferences = st.multiselect("Dietary Preferences", ["Vegetarian", "Vegan", "Paleo", "Keto", "Gluten-Free"])
        nutritional_goals = st.selectbox("Nutritional Goals", ["Weight Loss", "Muscle Gain", "Maintenance"])
        submit_button = st.form_submit_button(label="Save Profile")

        if submit_button:
            profile_data = {
                "name": name,
                "age": age,
                "weight": weight,
                "height": height,
                "dietary_preferences": dietary_preferences,
                "nutritional_goals": nutritional_goals
            }
            # Save user profile data
            if save_profile_data(profile_data):
                st.success("Profile saved successfully!")
            else:
                st.error("Failed to save profile. Please try again.")
