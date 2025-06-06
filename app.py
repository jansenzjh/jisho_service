from flask import Flask, render_template, request
import requests

app = Flask(__name__)

JISHO_API = "https://jisho.org/api/v1/search/words?keyword="

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    word = request.form['word']
    response = requests.get(JISHO_API + word)
    data = response.json()

    if data['data']:
        results = data['data']
    else:
        results = []

    return render_template('result.html', word=word, results=results)

if __name__ == '__main__':
    app.run(debug=True)
