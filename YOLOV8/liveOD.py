from ultralytics import solutions, YOLO
import streamlit as st

#solutions.inference()
model = YOLO('yolov5nu.pt')
### Make sure to run the file using command `streamlit run <file-name.py>`
st.write("hello ")
if(st.button("click me")):
    st.camera_input("take a pic")

