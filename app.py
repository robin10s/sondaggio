from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Pagina iniziale con il consenso informato
@app.route('/')
def consenso():
    return render_template('consenso.html')

# Pagina del quiz dopo il consenso
@app.route('/quiz')
def quiz():
    return render_template('index.html')

# Salvataggio delle risposte su Google Sheets tramite Sheet.best
@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    sheet_url = 'https://api.sheetbest.com/sheets/0ae1a0d6-e98b-421a-81d0-324450492f9c'

    # Invio dei dati al Google Sheet
    try:
        response = requests.post(sheet_url, json=data)
        response.raise_for_status()
        return jsonify({"status": "success"})
    except Exception as e:
        print(f"Errore durante l'invio: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
