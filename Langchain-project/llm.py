import streamlit as st
import time 
st.write("hello")
txt = st.text_input("write ur name")
st.write(f"length is {len(txt)}")

if(st.button("dont press")):
  st.write("why")

color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)
s =st.checkbox("hel")
if(s):
  
  st.warning("this is a warming",icon='🚨')
  
  st.balloons()
  
st.spinner("epkpsek")