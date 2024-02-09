# app.py

from flask import Flask, render_template, request, redirect, url_for
from Test import prediction

app = Flask(__name__)
app.static_folder = 'static'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'scanImage' not in request.files:
        return "error"

    file = request.files['scanImage']

    if file.filename == '':
        return redirect(url_for('upload'))

    # Save the uploaded file temporarily
    file_path = 'uploaded_image.jpg'
    file.save(file_path)

    # Call the DL model function
    prediction_result = prediction(file_path)

    # Redirect based on prediction
    if prediction_result == "1001":
        return redirect(url_for('negative'))
    else:
        return redirect(url_for('positive'))

@app.route('/positive')
def positive():
    return render_template('positive.html', prediction='Positive')


@app.route('/negative')
def negative():
    return render_template('negative.html', prediction='Negative')

if __name__ == '__main__':
    app.run(debug=True)
