from flask import Flask, jsonify, send_from_directory, render_template
import json
import os

app = Flask(__name__)

# Percorsi per audio tagliati (statici) e interi (dinamici)
AUDIO_STATIC_DIR = os.path.join(app.root_path, 'static', 'audio')
AUDIO_DINAMICO_DIR = os.path.join(app.root_path, 'static', 'audio_non_tagliati')

# Carica il file domande_6_audio.json
with open("domande.json", "r", encoding="utf-8") as f:
    domande = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/domande")
def get_domande():
    return jsonify(domande)

@app.route("/static/audio/<path:filename>")
def serve_audio_static(filename):
    return send_from_directory(AUDIO_STATIC_DIR, filename)

@app.route("/static/audio_non_tagliati/<path:filename>")
def serve_audio_dinamico(filename):
    return send_from_directory(AUDIO_DINAMICO_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True)
