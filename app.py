from flask import Flask, render_template, send_file
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download')
def download_file():
    return send_file('hf-logo.png', as_attachment=True)
