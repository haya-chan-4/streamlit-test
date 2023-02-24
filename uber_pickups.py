import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Uber pickups in NYC')

st.write('Display Image')

# if st.checkbox('show images'):
#     img = Image.open('town.jpg')
#     st.image(img, caption='town', use_column_width=True)

# option = st.selectbox('what do you like number?', list(range(1,11)))
# 'You like number is', option

hobby = st.text_input('What are your hobbies?')
'Your hobby is ', hobby

condition = st.slider('How are you doing?', 0, 100, 0)
'condition:', condition

