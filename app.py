from __future__ import division, print_function

import numpy as np

from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "-1" #Disabling GPU
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = 'mn1.h5'

# Load your trained model
model = load_model(MODEL_PATH)

print('Model loaded. Check http://127.0.0.1:5000/')


def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

   
    x = preprocess_input(x, mode='caffe')

    preds = model.predict(x)
    output = str(['Bed','Chair','Sofa'][preds[0].argmax()])
      # print(fn)
    print(output)
    

    
    return str(output)
   


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        print(basepath)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)

        return str(preds)
    return None


if __name__ == '__main__':
    app.run()

