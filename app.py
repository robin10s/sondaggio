from flask import Flask, render_template, request, jsonify
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json  # <-- Questo è una LISTA di risposte (10 risposte)
    if not os.path.exists("risposte"):
        os.makedirs("risposte")

    csv_file = "risposte/risposte.csv"

    # Se il file NON esiste, creiamo l'header
    file_exists = os.path.isfile(csv_file)

    with open(csv_file, "a", newline='', encoding="utf-8") as f:
        writer = None
        for risposta in data:
            if writer is None:
                # Scriviamo l'header una sola volta se il file è nuovo
                fieldnames = list(risposta.keys())
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                if not file_exists:
                    writer.writeheader()
            writer.writerow(risposta)

    return jsonify({"status": "ok"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
