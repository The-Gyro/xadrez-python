from flask_cors import CORS
from flask import Flask, request, jsonify, render_template
import main
import os
app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/board", methods=["GET"])
def board():
    return jsonify(main.board)

@app.route("/move", methods=["POST"])
def move():
    data = request.json
    return jsonify(main.processar_jogada(data["origem"], data["destino"]))

@app.route("/reset", methods=["POST"])
def reset():
    main.resetar_jogo()
    return jsonify({"ok": True})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)