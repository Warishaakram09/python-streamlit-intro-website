import streamlit as st

# Page settings
st.set_page_config(page_title="Python Info", page_icon="🐍", layout="centered")

# Title and subtitle
st.title("🐍 Welcome to Python World!")
st.subheader("Learn the Basics of Python Programming")

# Image with updated parameter
st.image("python-logo.png", caption="Python Logo", use_container_width=True)

# Description content
st.markdown("""
Python is a powerful, high-level programming language.  
It is used in web development, data science, automation, and much more!

### ✨ Key Features:
- Easy to read and write
- Huge community support
- Tons of libraries (like NumPy, Pandas, TensorFlow, etc.)

---

Made with ❤️ using **Streamlit**
""")

# Button interaction
if st.button("Click for a Python Tip!"):
    st.info("💡 Tip: Use list comprehensions for cleaner and faster loops in Python!")
