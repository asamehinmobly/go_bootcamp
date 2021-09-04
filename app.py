import json

from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/weather')
def get_weather_data():
    url = "https://www.7timer.info/bin/astro.php"

    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if lat and lon:
        query_string = {"ac": "0", "unit": "metric", "output": "json"}
        query_string.update({"lat": lat, "lon": lon})
        response = requests.request("GET", url, params=query_string)
        if response.status_code == 200:
            return json.loads(response.text)
        return {"response": "something went wrong"}
    else:
        return {"response": "check your request"}


if __name__ == '__main__':
    app.run()
