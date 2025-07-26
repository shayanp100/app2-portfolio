import streamlit as st
import pandas
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

content2 = """
Below you can find some of the apps I have built in Python
"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

