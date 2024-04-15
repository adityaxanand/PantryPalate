import streamlit as st

# Function to generate personalized greeting
def generate_greeting(name):
    if name:
        return f"Welcome back, {name}!"
    else:
        return "Welcome to Pantry Palate!"

# Function to fetch user data from the database (mocked for now)
def fetch_user_data(user_id):
    # Mocked user data for demonstration
    users_data = {
        "123": {"name": "John", "age": 30, "dietary_preferences": ["Vegetarian"], "nutritional_goals": "Weight Loss"},
        "456": {"name": "Emma", "age": 25, "dietary_preferences": ["Vegan", "Gluten-Free"], "nutritional_goals": "Maintenance"}
    }
    return users_data.get(user_id, None)

# Function to display personalized content on the home page
def show_home_page(user_id):
    user_data = fetch_user_data(user_id)
    if user_data:
        st.subheader(generate_greeting(user_data["name"]))
        st.write("Here are some personalized recommendations for you:")
        # Add personalized content based on user preferences
        if "Vegetarian" in user_data["dietary_preferences"]:
            st.write("- Try our new vegetarian recipes for a healthy meal plan.")
        if "Vegan" in user_data["dietary_preferences"]:
            st.write("- Explore our vegan-friendly options for a cruelty-free lifestyle.")
        if user_data["nutritional_goals"] == "Weight Loss":
            st.write("- Check out our low-calorie recipes to help you reach your weight loss goals.")
        if user_data["nutritional_goals"] == "Maintenance":
            st.write("- Maintain a balanced diet with our nutritious meal plans.")
    else:
        st.subheader(generate_greeting(None))
        st.write("Join Culinary Compass to unlock personalized meal planning, recipe suggestions, and more!")
        # Add call-to-action buttons or prompts for user registration/sign-up

# This part can be used for testing the home page locally without running the entire app
if __name__ == "__main__":
    user_id = "123"  # Mocked user ID for demonstration
    show_home_page(user_id)
