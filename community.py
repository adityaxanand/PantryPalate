import streamlit as st

# Function to fetch community recipes from a database or API
def fetch_community_recipes():
    # Mock community recipe data for demonstration
    community_recipes = [
        {
            "title": "Vegan Lentil Soup",
            "description": "A hearty and nutritious vegan soup, perfect for cold days.",
            "author": "JaneDoe",
            "likes": 35,
            "comments": 5
        },
        {
            "title": "Quinoa Salad with Mango and Avocado",
            "description": "A refreshing salad with a tropical twist, packed with flavor and nutrients.",
            "author": "HealthyEats123",
            "likes": 42,
            "comments": 8
        },
        {
            "title": "Vegetable Curry with Coconut Milk",
            "description": "A flavorful and comforting curry made with a variety of vegetables and creamy coconut milk.",
            "author": "SpiceMaster",
            "likes": 28,
            "comments": 3
        }
    ]
    return community_recipes

# Function to display the community page
def show_community_page():
    st.subheader("Community")
    st.write("Explore recipes shared by the Culinary Compass community!")

    # Fetch community recipes
    community_recipes = fetch_community_recipes()

    # Display community recipes
    for recipe in community_recipes:
        st.write("---")
        st.write(f"## {recipe['title']}")
        st.write(f"**Description:** {recipe['description']}")
        st.write(f"**Author:** {recipe['author']}")
        st.write(f"**Likes:** {recipe['likes']}  **Comments:** {recipe['comments']}")

# This part can be used for testing the community page locally without running the entire app
if __name__ == "__main__":
    show_community_page()
