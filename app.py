from flask import Flask, render_template, request, send_file
import requests

app = Flask(__name__)

PIXABAY_API_KEY = "#####api key #####3"


def search_pixabay_images(query):
    base_url = "https://pixabay.com/api/"
    params = {
        "key": PIXABAY_API_KEY,
        "q": query
    }
    response = requests.get(base_url, params=params)
    return response.json()


def search_pixabay_videos(query):
    base_url = "https://pixabay.com/api/videos/"
    params = {
        "key": PIXABAY_API_KEY,
        "q": query
    }
    response = requests.get(base_url, params=params)
    return response.json()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    search_type = request.form.get('type')
    
    if search_type == 'image':
        response = search_pixabay_images(query)
        results = response.get('hits', [])
        return render_template('results.html', results=results, media_type='image')
    elif search_type == 'video':
        response = search_pixabay_videos(query)
        results = response.get('hits', [])
        return render_template('results.html', results=results, media_type='video')


if __name__ == '__main__':
    app.run(debug=True)
