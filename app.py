from flask import Flask, render_template, request, jsonify
import json
import os
import csv
from datetime import datetime

app = Flask(__name__)

# Rotta per il consenso informato (pagina iniziale)
@app.route('/')
def consenso():
    return render_template('consenso.html')

# Rotta per il questionario (pagina del sondaggio)
@app.route('/quiz')
def quiz():
    return render_template('index.html')

# Rotta per ricevere i dati inviati dal sondaggio
@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    if not os.path.exists("risposte"):
        os.makedirs("risposte")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_path = os.path.join("risposte", "risposte.csv")
    file_exists = os.path.isfile(file_path)

    # Verifica che ci siano dati
    if not data:
        return jsonify({"status": "error", "message": "Nessun dato ricevuto"}), 400

    # Estrae i campi dal primo dizionario
    fieldnames = list(data[0].keys()) + ["timestamp"]

    try:
        with open(file_path, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            for row in data:
                row["timestamp"] = timestamp
                writer.writerow(row)
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
