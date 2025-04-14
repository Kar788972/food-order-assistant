
import streamlit as st
import requests

st.set_page_config(page_title="Food Prompt Assistant", layout="centered")
st.title("🍕 Unified Food Order Assistant")
st.markdown("Enter your food request in plain English, and we'll find the best options across platforms.")

user_prompt = st.text_input("What's your craving?")

if st.button("Find My Food") and user_prompt:
    with st.spinner("Thinking... 🍽️"):
        try:
            response = requests.post("http://localhost:8000/order", json={"prompt": user_prompt})
            if response.status_code == 200:
                data = response.json()
                st.subheader("🍴 Top Options")
                for option in data["top_options"]:
                    st.markdown(f"**{option['restaurant']}** on *{option['platform']}*")
                    st.markdown(f"- Item: {option['item']}\n- Price: AED {option['price']}\n- ETA: {option['eta']}\n- Rating: ⭐ {option['rating']}")
                    st.markdown("---")
                st.subheader("🧠 Parsed Order")
                st.code(data["parsed_order"], language="json")
            else:
                st.error("Failed to fetch options.")
        except Exception as e:
            st.error(f"Error: {e}")
