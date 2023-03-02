import streamlit as st
from location import locate
from PIL import Image

input_text = st.text_input('input text:', 'An ice cream near the door')
submit_button = st.form_submit_button('Submit')
if submit_button:
  locate(input_text)
  image = Image.open('final_canvas.jpg')
  st.image(image, caption='final_canvas')
