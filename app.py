import streamlit as st

st.title("tågstation")

st.header("välkommen")

st.subheader("biljettkiosk")

under_18 = 130
över_18 = 230
över_65 = 100

fråga_användaren_om_ålder = st.slider("skriv in din ålder")

if fråga_användaren_om_ålder <=18:
    st.write("130 kr")

elif fråga_användaren_om_ålder >=65:

    st.write("du ska betala 100 kr")

else:
    st.write("du ska betala 230 kr")
