from flask import Flask, request, jsonify
from flask_cors import CORS  # 👈 ADICIONA ISSO
import main

app = Flask(__name__)
CORS(app)  # 👈 E ISSO

@app.route("/board", methods=["GET"])
def board():
    return jsonify(main.board)

@app.route("/move", methods=["POST"])
def move():
    data = request.json
    origem = data["origem"]
    destino = data["destino"]

    return jsonify(main.processar_jogada(origem, destino))

import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)