from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"



if __name__ == '__main__':
    print("Starting Flask server on port 8080...")
    app.run(port=8080, debug=True)

