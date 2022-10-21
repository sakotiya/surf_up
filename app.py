from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    
    return "hello world"

@app.route("/normal")
def lets_fuck():
    return "Let's fuck baby"
#if__name__=="_main_"
