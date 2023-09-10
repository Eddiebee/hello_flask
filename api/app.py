from flask import Flask, render_template, send_file, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download_file', methods=['POST'])
def download_file():
    url = request.form['url']
    print(url)
    return send_file('hf-logo.png', as_attachment=True)
