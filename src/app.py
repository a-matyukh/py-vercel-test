from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '2'

@app.route('/about')
def about():
    return 'About'