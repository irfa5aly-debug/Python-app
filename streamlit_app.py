

import streamlit as st

st.set_page_config(
    page_title="Restaurant App",
    page_icon="🍽️",
    layout="wide"
)

# Restaurant heading
st.title("🍽️ Delicious Restaurant")
st.write("Welcome! Order your favorite food.")
st.divider()

# Food menu
menu = {
    "Burger": 450,
    "Pizza": 1200,
    "Biryani": 350,
    "Zinger Burger": 550,
    "French Fries": 200,
    "Cold Drink": 100
}

st.header("📋 Our Menu")

# Store quantities
if "cart" not in st.session_state:
    st.session_state.cart = {}

# Display menu
for food, price in menu.items():
    col1, col2, col3 = st.columns([3, 2, 2])

    with col1:
        st.subheader(food)

    with col2:
        st.write(f"Price: Rs. {price}")

    with col3:
        quantity = st.number_input(
            f"Quantity of {food}",
            min_value=0,
            max_value=20,
            value=st.session_state.cart.get(food, 0),
            key=food
        )
        st.session_state.cart[food] = quantity

st.divider()

# Calculate bill
st.header("🛒 Your Order")

total = 0

for food, quantity in st.session_state.cart.items():
    if quantity > 0:
        price = menu[food] * quantity
        total += price
        st.write(
            f"{food} × {quantity} = Rs. {price}"
        )

st.divider()

st.subheader(f"💰 Total Bill: Rs. {total}")

# Customer details
st.header("👤 Customer Details")

name = st.text_input("Customer Name")
phone = st.text_input("Phone Number")

order_type = st.radio(
    "Order Type",
    ["Dine In", "Takeaway", "Delivery"],
    horizontal=True
)

if st.button("✅ Place Order", type="primary"):
    if not name.strip():
        st.error("Please enter your name.")
    elif total == 0:
        st.error("Please select at least one food item.")
    else:
        st.success("Order placed successfully!")
        st.write(f"Customer: {name}")
        st.write(f"Order Type: {order_type}")
        st.write(f"Total Amount: Rs. {total}")
        st.write("Thank you for visiting Delicious Restaurant! ❤️")
