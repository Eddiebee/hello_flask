from flask import Flask, render_template, send_file, request
import requests
from dotenv import load_dotenv

import os

app = Flask(__name__)

# load the environment variables from the .env file
load_dotenv()


@app.route('/')
def home():
    url = "https://api.apollo.io/v1/labels"

    querystring = {
        "api_key": os.environ["API_KEY"]
    }

    headers = {
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json'
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    labels = response.json()

    return render_template('index.html', labels=labels)


@app.route('/download_file', methods=['POST'])
def download_file():
    url = request.form['url']
    # label_id = request.form['url']
    print(url)
    return send_file('hf-logo.png', as_attachment=True)
