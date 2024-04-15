import streamlit as st

# Function to save user's inventory data to a file or database
def save_inventory_data(user_id, inventory_data):
    # Code to save the inventory data (mocked for now)
    with open(f"user_{user_id}_inventory.txt", "w") as file:
        for item in inventory_data:
            file.write(item + "\n")
    return True

# Function to display the user's inventory page
def show_inventory_page(user_id):
    st.subheader("Inventory")
    st.write("Manage your ingredient inventory here.")

    # Display form to input inventory items
    with st.form("inventory_form"):
        st.write("Add items to your inventory:")
        new_item = st.text_input("Enter item")
        add_button = st.form_submit_button("Add")

    # Handle addition of new item to inventory
    if add_button:
        # Fetch existing inventory data
        inventory_data = []
        try:
            with open(f"user_{user_id}_inventory.txt", "r") as file:
                inventory_data = file.read().splitlines()
        except FileNotFoundError:
            pass  # File not found, likely because user doesn't have any inventory yet
        
        # Add new item to inventory
        inventory_data.append(new_item)

        # Save updated inventory data
        if save_inventory_data(user_id, inventory_data):
            st.success("Item added to inventory successfully!")
        else:
            st.error("Failed to add item to inventory. Please try again.")

    # Display current inventory list
    st.write("Your current inventory:")
    try:
        with open(f"user_{user_id}_inventory.txt", "r") as file:
            inventory_data = file.read().splitlines()
            for item in inventory_data:
                st.write(f"- {item}")
    except FileNotFoundError:
        st.write("Your inventory is empty.")
