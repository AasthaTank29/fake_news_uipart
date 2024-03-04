import streamlit as st

st.title("Bullet Points with Links Example")

# Define bullet points and their corresponding links
bullet_points = {
    "First Point": "https://www.example.com/first",
    "Second Point": "https://www.example.com/second",
    "Third Point": "https://www.example.com/third"
}

# Split bullet points into four parts
num_parts = 4
points_per_part = len(bullet_points) // num_parts

# Create a container for the bullet points in the upper right corner
container = st.beta_container()
container.markdown(
    """
    <style>
    .st-b9 {
        position: absolute;
        top: 10px;
        right: 10px;
    }
    </style>
    """
)

# Display bullet points with links in the container
with container:
    for i in range(num_parts):
        st.write(f"Part {i+1}:")
        for point, link in list(bullet_points.items())[i*points_per_part:(i+1)*points_per_part]:
            st.markdown(f"- [{point}]({link})")
