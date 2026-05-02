from flask import Flask, request, jsonify
from flask_cors import CORS
import main
import os

app = Flask(__name__)
CORS(app)


@app.route("/board", methods=["GET"])
def board():
    return jsonify(main.board)


@app.route("/move", methods=["POST"])
def move():
    data = request.json
    origem = data["origem"]
    destino = data["destino"]

    return jsonify(main.processar_jogada(origem, destino))


@app.route("/reset", methods=["GET", "POST"])
def reset():
    main.resetar_jogo()
    return jsonify({"ok": True})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)