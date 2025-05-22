from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import json
import os

app = Flask(__name__)
app.secret_key = 'chave-secreta'

ranking = 'ranking.json'

def load_scores():
    if not os.path.exists(ranking):  
        return []
    with open(ranking, 'r') as f:
        return json.load(f)

def save_score(score):
    scores = load_scores()
    scores.append(score)
    scores = sorted(scores, key=lambda x: x['score'], reverse=True)[:7]
    with open(ranking, 'w') as f:
        json.dump(scores, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    skin = session.get('skin', 'images/ryan1.jpg')
    return render_template('game.html', skin_path=skin)

@app.route('/skins')
def skins():
    return render_template('skins.html')

@app.route('/selecionar_skin/<nome>')
def selecionar_skin(nome):
    session['skin'] = f'images/{nome}'
    return redirect(url_for('game'))

@app.route('/leaderboard')
def leaderboard():
    scores = load_scores()
    return render_template('leaderboard.html', scores=scores)

@app.route('/enviar_pontuacao', methods=['POST'])
def enviar_pontuacao():
    data = request.json
    save_score({"name": data['nome'], "score": data['score']})
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
