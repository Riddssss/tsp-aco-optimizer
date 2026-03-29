from flask import Flask, jsonify
from flask_cors import CORS
from src.ant_system import ant_system
from src.max_min_as import max_min_as

app = Flask(__name__)
CORS(app)

# 🔥 helper to clean numpy types
def clean_tour(tour):
    return [int(x) for x in tour]

@app.route('/as')
def run_as():
    tour, length, _ = ant_system()
    return jsonify({
        "tour": clean_tour(tour),
        "length": int(length)
    })

@app.route('/mmas')
def run_mmas():
    tour, length, _ = max_min_as()
    return jsonify({
        "tour": clean_tour(tour),
        "length": int(length)
    })

app.run(debug=True)