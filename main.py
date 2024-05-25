import streamlit as st
import pandas as pd

#col0 = st.columns(1)

#with col0:
#    st.title("""My Introduction""")

col1, col2 = st.columns(2)
with col1:
    
    st.image("images/photo.png")

with col2:
    
    content = '''
        Welcome to my digital portfolio, where I'm excited to share some of my personal projects I've worked on as a Python developer. As someone who is passionate about using code to solve 
        real-world problems and create positive change, I believe that showcasing my projects in one place can help others learn from my experiences, get inspired by new ideas, and maybe even pick up a few tips and 
        tricks along the way. From data analysis tools to machine learning models, and from web applications to command-line utilities, each project on this site represents a unique opportunity for me to explore the 
        possibilities of Python programming and share that knowledge with others. So take a look around, browse through the projects, and let me know what you think - I'm always eager to hear feedback and learn more 
        about how I can use my skills to make a positive impact!
    '''
    st.info(content)

content2 = "Below are some of the apps that I have built!"
st.info(content2)

col3, col4 = st.columns(2)

df = pd.read_csv('data.csv', sep=';')

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
