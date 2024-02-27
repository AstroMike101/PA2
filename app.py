from flask import Flask, request, redirect, render_template
import os
import subprocess
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
#uploads
def upload_file():
    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    #rename
    os.rename(filepath, os.path.join(app.config['UPLOAD_FOLDER'], 'walk.cc'))
    
    #runs code
    compilation_result = subprocess.run(['python3', 'compile.py'], capture_output=True, text=True)
    
    score = compilation_result.stdout
    return render_template('result.html', score=score)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
