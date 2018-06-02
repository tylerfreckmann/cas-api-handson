from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
import os
from werkzeug.utils import secure_filename
import swat
import requests
from collections import OrderedDict

APP_IP = '0.0.0.0'
APP_PORT = 7050
AUTHINFO = './.authinfo'
UPLOAD_FOLDER = '/imgcaslib'
ASTORE_LIB = 'casuser'
ASTORE = 'lenet'
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(url_for('index'))
        file = request.files['file']
        if file.filename == '':
            print('No selected file')
            return redirect(url_for('index'))
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # CAS Image Recognition

            # FILL IN THE FOLLOWING COMMENTS WITH CODE THAT DOES WHAT EACH LINE DESCRIBES
            # create a CAS session on localhost:5570 with your CAS user
            # load the image action set
            # load the image from the filepath into CAS
            # load the astore action set
            # score the image table you created with the ASTORE in ASTORE_LIB
            # fetch the score results from the score table you created in CAS
            # isolate the Fetch object from the score results, get the first row, turn it into a python dictionary, and save it to a variable names scores
            # end the CAS session

            # the rest should be good to go :)
            label = scores.pop('I__label_')
            return jsonify({'imgUrl': url_for('uploaded_file', filename=filename),
                'label': label,
                'scores': scores})

    return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True, host=APP_IP, port=APP_PORT)