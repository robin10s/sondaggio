from flask import Flask, render_template, request, jsonify
import os
import json
import requests

app = Flask(__name__)

@app.route('/')
def consenso():
    return render_template('consenso.html')  # Pagina iniziale con consenso informato

@app.route('/survey')
def survey():
    return render_template('index.html')  # Pagina con il sondaggio

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    SHEET_BEST_URL = "https://sheet.best/api/sheets/INSERISCI-LINK-QUI"  # Sostituisci con il tuo link

    for riga in data:
        res = requests.post(SHEET_BEST_URL, json=riga)
        print("Inviato:", res.status_code)

    return jsonify({"status": "ok"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
