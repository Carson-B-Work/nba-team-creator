from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Welcome to the NBA Team Creator!</h1>'