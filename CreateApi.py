from flask import Flask, jsonify
import requests

topic = 'pizza'

r = requests.get(f"https://newsdata.io/api/1/latest?apikey=pub_544091257deffd722ec22e69b071d893fdb3b&q={topic}")

app = Flask(__name__)

@app.route('/')
def get_api():
    response = {'result': r.json()}
    return jsonify(response)

app.run(port=5000)


