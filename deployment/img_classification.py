import keras
from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf


def import_and_predict(img, weights_file):
    # Load the model
    model = keras.models.load_model(weights_file)

    # Create the array of the right shape to feed into the keras model
    data = tf.keras.preprocessing.image.img_to_array(img)
    data = np.ndarray(shape=(1, 227, 227, 3), dtype=np.float32)
    #data = np.ndarray(data)
    image = img
    #image sizing
    size = (227, 227)
    
    #return a resized and cropped version of the image
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = image_array.astype(np.float32) / 255.

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    return prediction[0] # return position of the highest probability