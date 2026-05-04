# python3 -m venv $HOME/venv
# source $HOME/venv/bin/activate
# python3 -m pip install flask
# python3 static.py
# http://127.0.0.1:5000
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)