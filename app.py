from flask import Flask, render_template, request, jsonify
import json
from datubaze import get_top_results, pievienot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/game')
def game():
    return render_template("game.html")

@app.route('/top')
def top():
    return render_template("top.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/topData', methods=['GET'])
def top_data():
    try:
        top_rezultati = get_top_results()
        top_5 = sorted(top_rezultati, key=lambda x: (x['klikski'], x['laiks']))[:5]
        return jsonify(top_5), 200
    except Exception:
        return jsonify({'status': 'error'}), 500
    
@app.route('/pievienot-rezultatu', methods=['POST'])
def pievinot_rezultatu():
    dati = request.json
    try:
        pievienot(dati)
        
    

if __name__ == '__main__':
  app.run(debug=True)

