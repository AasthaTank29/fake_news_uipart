import streamlit as st

st.title("Bullet Points with Links Example")

# Define bullet points and their corresponding links
bullet_points = {
    "First Point": "https://www.example.com/first",
    "Second Point": "https://www.example.com/second",
    "Third Point": "https://www.example.com/third"
}

# Display bullet points with links
for point, link in bullet_points.items():
    st.markdown(f"- [{point}]({link})")
