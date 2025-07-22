import streamlit as st

# Title of the app
st.title("🍽️ Simple Food Recommendation System")

# Ask the user what kind of food they want
choice = st.selectbox("What kind of food are you in the mood for?", 
                      ["Select one", "Breakfast", "Lunch", "Dinner", "Comfort Food", "Healthy", "Sweet"])

# Recommend food based on choice
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

# Show recommendation
if choice != "Select one":
    st.success(recommend_food(choice))
