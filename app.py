import streamlit as st

st.title("Ksenia's first Hackathon app")

click = st.button("Click for magic ✨")
if click:
    st.balloons()

pick = st.radio("Choose your magic",["Flying","Making dinner instantly","Sleep forever"])
st.write("You chose",pick)

select = st.checkbox("I want all the magic in the world")
select
