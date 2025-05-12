from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/")
def consenso():
    return render_template("consenso.html")

@app.route("/quiz")
def quiz():
    return render_template("index.html")

@app.route("/finale")
def finale():
    return render_template("finale.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    try:
        response = requests.post(
            "https://api.sheetbest.com/sheets/0ae1a0d6-e98b-421a-81d0-324450492f9c",
            json=data
        )
        return jsonify({"status": "success", "sheet_response": response.status_code})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
