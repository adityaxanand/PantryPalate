import streamlit as st

# Mock recipe data for demonstration
recipes_data = [
    {
        "title": "Vegan Buddha Bowl",
        "description": "A delicious and nutritious vegan meal in a bowl!",
        "ingredients": ["Quinoa", "Mixed greens", "Chickpeas", "Avocado", "Carrots", "Cucumber", "Tahini dressing"],
        "instructions": "1. Cook quinoa according to package instructions. 2. Chop vegetables and avocado. 3. Assemble ingredients in a bowl. 4. Drizzle with tahini dressing.",
        "image": "https://www.example.com/vegan_buddha_bowl.jpg"
    },
    {
        "title": "Mediterranean Chickpea Salad",
        "description": "A refreshing and flavorful salad with Mediterranean-inspired ingredients.",
        "ingredients": ["Chickpeas", "Tomatoes", "Cucumbers", "Red onion", "Feta cheese", "Kalamata olives", "Olive oil", "Lemon juice", "Fresh herbs"],
        "instructions": "1. Combine all ingredients in a large bowl. 2. Toss with olive oil, lemon juice, and herbs. 3. Serve chilled.",
        "image": "https://www.example.com/mediterranean_chickpea_salad.jpg"
    }
]

# Function to display recipe suggestions
def show_recipes_page():
    st.subheader("Recipes")
    st.write("Discover delicious recipes to inspire your culinary journey!")

    # Display recipe cards
    for recipe in recipes_data:
        st.write("---")
        st.write(f"## {recipe['title']}")
        st.image(recipe["image"], caption=recipe["description"], use_column_width=True)
        st.write("**Ingredients:**")
        for ingredient in recipe["ingredients"]:
            st.write(f"- {ingredient}")
        st.write("**Instructions:**")
        st.write(recipe["instructions"])
