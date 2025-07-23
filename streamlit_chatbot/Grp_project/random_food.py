import streamlit as st
import random

st.title("🍽️ Simple Food Recommendation System")

# Choose food mood
choice = st.selectbox("What kind of food are you in the mood for?", 
                      ["Select one", "Breakfast", "Lunch", "Dinner", "Comfort Food", "Healthy", "Sweet"])

def recommend_food(option):
    if option == "Breakfast":
        return "🥞 Try pancakes and scrambled eggs!"
    elif option == "Lunch":
        return "🍛 How about chicken rice or a sandwich?"
    elif option == "Dinner":
        return "🍝 Maybe spaghetti or grilled salmon?"
    elif option == "Comfort Food":
        return "🍔 Go for mac & cheese or fried chicken!"
    elif option == "Healthy":
        return "🥗 A quinoa salad or grilled veggies would be great!"
    elif option == "Sweet":
        return "🍦 Try waffles, cake, or bubble tea!"
    else:
        return ""

# Show mood-based recommendation
if choice != "Select one":
    st.success(recommend_food(choice))

# List of random food options
food_list = [
    "🍕 Pizza", "🍣 Sushi", "🍜 Ramen", "🍛 Nasi Lemak", "🥗 Caesar Salad",
    "🍔 Burger", "🍰 Cheesecake", "🥪 Sandwich", "🍝 Spaghetti", "🍤 Fried Prawns"
]

# Show random recommendation
if st.button("🎲 Give me a random food suggestion!"):
    random_food = random.choice(food_list)
    st.success(f"How about: {random_food}?")

# --- Beverage Recommendation Section ---
st.header("🥤 Beverage Recommendation System")

# Dropdown
drink_choice = st.selectbox("What kind of drink would you like?", 
                            ["Select one", "Hot", "Cold", "Healthy", "Sweet", "Caffeinated"])

def recommend_drink(drink_type):
    if drink_type == "Hot":
        return "☕ How about a cup of hot chocolate or tea?"
    elif drink_type == "Cold":
        return "🥤 Try iced lemon tea or a chilled soda!"
    elif drink_type == "Healthy":
        return "🍵 Maybe a green smoothie or coconut water!"
    elif drink_type == "Sweet":
        return "🧋 Try bubble tea or a caramel frappe!"
    elif drink_type == "Caffeinated":
        return "☕ A nice cup of coffee or espresso will do!"
    else:
        return ""

if drink_choice != "Select one":
    st.success(recommend_drink(drink_choice))

# Random drink suggestion
drink_list = [
    "🧋 Bubble Tea", "☕ Coffee", "🍹 Mojito", "🍵 Matcha Latte",
    "🥤 Cola", "🍊 Orange Juice", "🥛 Milkshake", "🧃 Apple Juice"
]

if st.button("🎲 Give me a random drink suggestion!"):
    random_drink = random.choice(drink_list)
    st.success(f"How about: {random_drink}?")


