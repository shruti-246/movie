import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Add a route for the root URL
@app.route('/')
def home():
    return "Welcome to the Movie API! Use /api/movie?title={your_movie_title} to get movie information."

@app.route('/api/movie', methods=['GET'])
def get_movie():
    title = request.args.get('title')  # Get the movie title from the request parameters
    api_key = os.getenv('OMDB_API_KEY')  # Retrieve API key from environment variables

    if not title:
        return jsonify({'error': 'Title parameter is required'}), 400

    # Construct the request URL for the OMDb API
    url = f'http://www.omdbapi.com/?t={title}&apikey={api_key}'

    # Make a request to the OMDb API
    response = requests.get(url)
    if response.status_code == 200:
        movie_data = response.json()
        if movie_data['Response'] == 'True':
            return jsonify(movie_data)  # Return movie data as JSON
        else:
            return jsonify({'error': movie_data['Error']}), 404  # Handle errors from the API
    else:
        return jsonify({'error': 'Failed to fetch movie data'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)

