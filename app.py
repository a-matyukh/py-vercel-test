from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '1'

@app.route('/about')
def about():
    return 'About'