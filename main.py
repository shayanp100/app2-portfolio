import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """
    Hey, I am Shayan and I am an aspiring Software engineer.
    I am expected to graduate in June 2026 with a first class
    honours BSc in Computer Science. My main interest is in 
    the field of quantitative finance.
    """
    st.info(content)