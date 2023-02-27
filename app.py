import streamlit as st

st.title("Arif Basha Data APP")
st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.balloons()