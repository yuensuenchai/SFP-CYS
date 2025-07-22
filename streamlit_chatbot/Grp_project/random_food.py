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
