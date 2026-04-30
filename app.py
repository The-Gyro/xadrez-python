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

app.run(debug=True)