import streamlit as st

# Mock function to generate shopping list based on meal plan
def generate_shopping_list(meal_plan_data):
    shopping_list = {}
    for meals in meal_plan_data.values():
        for meal in meals:
            ingredients = get_ingredients_for_meal(meal)
            for ingredient in ingredients:
                shopping_list[ingredient] = shopping_list.get(ingredient, 0) + 1
    return shopping_list

# Mock function to fetch ingredients for a meal from a database or API
def get_ingredients_for_meal(meal):
    # Mocked ingredient data for demonstration
    ingredients_mapping = {
        "Vegan Buddha Bowl": ["Quinoa", "Mixed greens", "Chickpeas", "Avocado", "Carrots", "Cucumber", "Tahini dressing"],
        "Mediterranean Chickpea Salad": ["Chickpeas", "Tomatoes", "Cucumbers", "Red onion", "Feta cheese", "Kalamata olives", "Olive oil", "Lemon juice", "Fresh herbs"],
        "Stuffed Bell Peppers": ["Bell peppers", "Quinoa", "Black beans", "Corn", "Tomatoes", "Onion", "Garlic", "Spices"],
        "Quinoa Salad with Roasted Vegetables": ["Quinoa", "Bell peppers", "Zucchini", "Cherry tomatoes", "Red onion", "Balsamic vinegar", "Olive oil", "Herbs"],
        "Vegetable Stir-Fry": ["Tofu", "Mixed vegetables", "Soy sauce", "Sesame oil", "Garlic", "Ginger", "Rice"],
        "Black Bean Tacos": ["Black beans", "Tortillas", "Avocado", "Lettuce", "Tomatoes", "Onion", "Cilantro", "Lime"],
        "Pasta Primavera": ["Pasta", "Broccoli", "Carrots", "Bell peppers", "Zucchini", "Cherry tomatoes", "Garlic", "Olive oil", "Parmesan cheese"],
        "Caprese Salad": ["Tomatoes", "Fresh mozzarella", "Basil", "Balsamic vinegar", "Olive oil", "Salt", "Pepper"],
        "Thai Curry with Tofu": ["Tofu", "Coconut milk", "Curry paste", "Mixed vegetables", "Rice"],
        "Greek Lentil Soup": ["Lentils", "Tomatoes", "Carrots", "Celery", "Onion", "Garlic", "Vegetable broth", "Herbs", "Lemon"],
        "Falafel Wrap": ["Falafel", "Pita bread", "Hummus", "Cucumber", "Tomato", "Lettuce", "Tahini sauce"],
        "Ratatouille": ["Eggplant", "Zucchini", "Tomatoes", "Onion", "Garlic", "Herbs", "Olive oil"],
        "Vegetarian Chili": ["Kidney beans", "Black beans", "Tomatoes", "Bell peppers", "Onion", "Garlic", "Chili powder", "Cumin"],
        "Cauliflower Alfredo Pasta": ["Cauliflower", "Pasta", "Garlic", "Almond milk", "Nutritional yeast", "Olive oil", "Salt", "Pepper"]
    }
    return ingredients_mapping.get(meal, [])

# Function to display the user's shopping list page
def show_shopping_list_page(meal_plan_data):
    st.subheader("Shopping List")
    st.write("Here's your shopping list based on your meal plan:")

    # Generate shopping list
    shopping_list = generate_shopping_list(meal_plan_data)

    # Display shopping list
    if shopping_list:
        for item, quantity in shopping_list.items():
            st.write(f"- {item}: {quantity}")
    else:
        st.write("Your shopping list is empty. Start planning your meals!")
