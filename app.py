import flask
import os
import requests
import json

app = flask.Flask(__name__)
API_KEY = os.getenv("GENIUS_KEY")
url = 'https://api.genius.com/search?q=Kendrick%20Lamar'

my_headers = {
    "Authorization": "Bearer " + str(API_KEY)
}

response = requests.get(url, headers=my_headers)
data = response.json()
print(json.dumps(response.json(), indent=4))

@app.route('/')
def index():
    test_content = data["response"]["hits"][0]
    return flask.render_template(
        "index.html",
        test=test_content
    )
app.run(
    port=int(os.getenv('PORT', 3000)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)
