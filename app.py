from flask import Flask, request
from werkzeug.utils import secure_filename
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)




CORS(app)
cors = CORS(app, resources = {
    r"*":{
        "origins": "*"
    }
})

@app.route('/')
def home():
    return {
        'ok': True
    }

@app.route('/upload_file', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files)
        f = request.files['file']
        var_name = request.form['var_name']

        now = datetime.now()

        saved_name = f'{var_name}-{now.strftime("%m/%d/%Y, %H:%M:%S")}-{f.filename}'
        f.save(secure_filename(saved_name))
        return {
            'ok': True,
            'file_name': saved_name
        }
   

@app.route('/getForm', methods=['POST'])
def getForm():
    if request.method == 'POST':
        form = request.form
        files = request.files

        data = {
            'cover': files.get('cover'),
            'name': form.get('name'),
            'surname': form.get('surname'),
            'phone': form.get('phone')
        }

        print(data)

    return {
        'ok': True
    }


if __name__ == '__main__':
    app.run(debug=True)