import os
import sys

# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Some utilites
import numpy as np
from util import base64_to_pil


# Declare a flask app
app = Flask(__name__)


# You can use pretrained model from Keras
# Check https://keras.io/applications/
# or https://www.tensorflow.org/api_docs/python/tf/keras/applications

#from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
#model = MobileNetV2(weights='imagenet')

# Model saved with Keras model.save()
MODEL_PATH = 'models/leukoRight.h5'

# Load your own trained model
model = load_model(MODEL_PATH)
model.make_predict_function()          # Necessary
print('Model loaded. Start serving...')

print('Model loaded. Check http://127.0.0.1:5000/')

#def model_predict(img, model):
#    img = img.resize((512, 512))
#
#    # Preprocessing the image
#    x = image.img_to_array(img)
#    # x = np.true_divide(x, 255)
#    x = np.expand_dims(x, axis=0)
#
#    # Be careful how your trained model deals with the input
#    # otherwise, it won't make correct prediction!
#    x = preprocess_input(x, mode='tf')
#
#    preds = model.predict(x)
#    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
    
        image_size = (512, 512)

        img = base64_to_pil(request.json)

        #img.save("./uploads/image.png")

        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)  # Create batch axis

        predictions = model.predict(img_array)

        theWBC = str(np.argmax(predictions))

        overall = np.sum(predictions)

        theValue = str(np.amax(predictions))

        wbc_lookup = dict([
                ('0','artifact'),
                ('1','band neutrophil'),
                ('2','basophil'),
                ('3','bursted cell'),
                ('4','eosinophil'),
                ('5','large lympthocyte'),
                ('6','metamyelocyte'),
                ('7','monocyte'),
                ('8','neutrophil'),
                ('9','nRBC'),
                ('10','small lymphocyte')
        ])

        wbcName = str(wbc_lookup[theWBC])

        return jsonify(result=wbcName, probability=theValue)

    return None


if __name__ == '__main__':
    # app.run(port=5002, threaded=False)

    # Serve the app with gevent
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
