from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

ranking = 'ranking.json'

def load_scores():
    if not os.path.exists(ranking):
        return []
    with open(ranking, 'r') as f:
        return json.load(f)

def save_score(score):
    scores = load_scores()
    scores.append(score)
    scores = sorted(scores, key=lambda x: x['score'], reverse=True)[:7]  # top 7
    with open(ranking, 'w') as f:
        json.dump(scores, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/skins')
def skins():
    return render_template('skins.html')

@app.route('/leaderboard')
def leaderboard():
    scores = load_scores()
    return render_template('leaderboard.html', scores=scores)

@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.json
    save_score({"name": data['name'], "score": data['score']})
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
