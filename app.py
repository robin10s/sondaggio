from flask import Flask, render_template, request, jsonify
import json
import os
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json

    # Assicura che la cartella 'risposte' esista
    if not os.path.exists("risposte"):
        os.makedirs("risposte")

    # ✅ 1️⃣ Salva in JSON (come array di oggetti)
    json_path = "risposte/risposte.json"
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    existing_data.append(data)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    # ✅ 2️⃣ Salva anche in CSV
    csv_path = "risposte/risposte.csv"
    csv_columns = list(data.keys())

    file_exists = os.path.exists(csv_path)

    with open(csv_path, "a", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)

        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

    return jsonify({"status": "ok"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
