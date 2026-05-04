# python3 -m venv $HOME/venv
# source $HOME/venv/bin/activate
# python3 -m pip install flask
# python3 rest.py
# http://127.0.0.1:5000

from flask import Flask, jsonify, request

app = Flask(__name__)

users = []

# curl http://127.0.0.1:5000/users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d '{"name": "John Doe"}'
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    users.append(data)
    return jsonify({"message": "User created", "user": data})

if __name__ == "__main__":
    app.run(debug=True)