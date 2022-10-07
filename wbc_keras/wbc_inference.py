import tensorflow as tf
import numpy as np
import keras_cv
import os
import sys
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow import keras
from keras.models import load_model
from tensorflow.keras import layers
from tensorflow.python.client import device_lib
import matplotlib.pyplot as plt

#-----------------------------------------------------------------------------------

#inference

image_size = (512, 512)

model = load_model('leukoRight.h5')
img = keras.preprocessing.image.load_img(
    sys.argv[1], target_size=image_size
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create batch axis

predictions = model.predict(img_array)

theWBC = np.argmax(predictions)

overall = np.sum(predictions)

theValue = np.amax(predictions)

percentWBC = round((theValue / overall)*100,4)

print("{} - {}\n{}".format(theWBC,percentWBC,predictions))



