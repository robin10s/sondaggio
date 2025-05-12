from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json

    SHEET_BEST_URL = "https://api.sheetbest.com/sheets/0ae1a0d6-e98b-421a-81d0-324450492f9c"

    for riga in data:
        res = requests.post(SHEET_BEST_URL, json=riga)
        print("Inviato:", res.status_code)

    return jsonify({"status": "ok"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
