from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/place.html')
def place():
    return render_template('place.html')


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"message": "Missing email or password"}), 400

    if data['email'] == 'test@example.com' and data['password'] == 'testpassword':
        return jsonify({"access_token": "mock-jwt-token"}), 200

    return jsonify({"message": "Invalid credentials"}), 401


@app.route('/places/<place_id>', methods=['GET'])
def get_place_details(place_id):
    try:
        with open('data/places.json', 'r') as file:
            places = json.load(file)

        place = next((p for p in places if p["id"] == place_id), None)
        if place:
            return jsonify(place), 200
        else:
            return jsonify({"error": "Place not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
