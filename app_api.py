import streamlit as st
from location import locate
from PIL import Image

form1 = st.form(key='my_form1')
input_text = form1.text_input('input text:', 'An ice cream near the door')
submit_button = form1.form_submit_button(label = 'Submit')
if submit_button:
  locate(input_text)
  image = Image.open('final_canvas.jpg')
  st.image(image, caption='final_canvas')
