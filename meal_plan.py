import streamlit as st

# Mock meal plan data for demonstration
meal_plan_data = {
    "Monday": ["Vegan Buddha Bowl", "Mediterranean Chickpea Salad"],
    "Tuesday": ["Stuffed Bell Peppers", "Quinoa Salad with Roasted Vegetables"],
    "Wednesday": ["Vegetable Stir-Fry", "Black Bean Tacos"],
    "Thursday": ["Pasta Primavera", "Caprese Salad"],
    "Friday": ["Thai Curry with Tofu", "Greek Lentil Soup"],
    "Saturday": ["Falafel Wrap", "Ratatouille"],
    "Sunday": ["Vegetarian Chili", "Cauliflower Alfredo Pasta"]
}

# Function to display the user's meal plan page
def show_meal_plan_page():
    st.subheader("Meal Plan")
    st.write("Plan your meals for the week here.")

    # Display meal plan for each day of the week
    for day, meals in meal_plan_data.items():
        st.write(f"### {day}")
        if meals:
            for i, meal in enumerate(meals, start=1):
                st.write(f"{i}. {meal}")
        else:
            st.write("No meal planned for this day.")

    # Add option to customize meal plan
    st.write("Customize your meal plan:")
    new_meal = st.text_input("Enter new meal")
    day_dropdown = st.selectbox("Select day to add meal", list(meal_plan_data.keys()))
    add_button = st.button("Add Meal")

    # Handle addition of new meal to meal plan
    if add_button and new_meal:
        meal_plan_data[day_dropdown].append(new_meal)
        st.success("Meal added to meal plan successfully!")
