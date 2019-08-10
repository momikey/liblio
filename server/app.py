# Sample to test Flask installation

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, world!"
