import flask
import os
import requests
import json
import random

app = flask.Flask(__name__)
API_KEY = os.getenv("GENIUS_KEY")
url = 'https://api.genius.com/search?q=Nat%20King%20Cole%20Love'

my_headers = {
    "Authorization": "Bearer " + str(API_KEY)
}

response = requests.get(url, headers=my_headers)
data = response.json()


#DEBUG ONLY -- delete later
# with open('response-sample.json') as f:
#     data = json.load(f)
# END DEBUG

print(json.dumps(data, indent=4))

@app.route('/')
def index():
    base = data["response"]["hits"]
    test_content = base[0]
    range = len(base)
    randomNum = random.randrange(0,range)
    image = base[randomNum]["result"]["song_art_image_url"]
    song_title = base[randomNum]["result"]["title"]
    artist_link = base[randomNum]["result"]["primary_artist"]["url"]
    artist_profile = base[randomNum]["result"]["primary_artist"]["image_url"]

    return flask.render_template(
        "index.html",
        test=test_content,
        maxPossible=range,
        digit=randomNum,
        songURL=image,
        artistLink=artist_link,
        title = song_title,
        profileURL= artist_profile
    )
app.run(
    port=int(os.getenv('PORT', 3000)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)
