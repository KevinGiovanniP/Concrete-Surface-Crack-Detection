import streamlit as st
import keras
from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf
from img_classification import import_and_predict


def app():
    st.write('Image Classification with Tensorflow')
    st.header('Welcome, Lets detect cracked surface, shall we? 😁')
    st.text('Upload Crack Surface Image for Image classification as Cracked or Not Crack')

    
    st.markdown(
        "<h1 style='text-align: center'>🔨 Concrete Crack Surface Detection 🔨</h1>",
        unsafe_allow_html=True,
    )

    model = tf.keras.models.load_model("Crack_Detection_model.h5")
    img_data = st.file_uploader(label='please load image for detection below ⬇️ ', type=['png','jpg'])
    if img_data is not None:
        image = Image.open(img_data)
        st.image(image, caption='Uploaded Concrete Image', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        label = import_and_predict(image, 'Crack_Detection_model.h5')
        if st.button("Generate Prediction"):
            if label >= 0.5:
                st.write("The surface is cracked, thanks god its not passed  😥 ")
            else:
                st.write("The surface is absolutely fine, no need to worry for all that crack 🥳 ")
        
    