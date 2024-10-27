from flask import Flask, render_template, request
import requests

app = Flask(__name__)

OMDB_API_KEY = 'b66b763b'  # Replace with your OMDB API key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.form['movie_name']
    response = requests.get(f"http://www.omdbapi.com/?t={movie_name}&apikey={OMDB_API_KEY}")
    data = response.json()

    if data['Response'] == 'True':
        return render_template('results.html', movie=data)
    else:
        return render_template('results.html', error=data['Error'])

if __name__ == '__main__':
    app.run(debug=True)

