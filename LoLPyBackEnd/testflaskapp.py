'''
Test Flask App
Development flask site for LoLPyBackEnd
'''

from flask import Flask, request, url_for, jsonify
import requests

# Application declaration
app = Flask(__name__)
app.secret_key = 'This is really unique and secret'

# Test relevant parameters
API_KEY = "?api_key=e20154f8-3601-40ac-ae35-5af13e62cc8c"
TARGET_URL = "https://euw.api.pvp.net/api/lol/euw/v1.4/summoner/by-name/NadsOfMahen"

# Route stuff

# home/root
@app.route('/')
def hello_world():
	return "Hello ... World!"

@app.route('/name_test')
def name_test():
	return "Worked!"

# testing variable/dynamic urls
@app.route('/<path:added_url>')
def reroute(added_url):
	#new_url = unicode.encode((added_url+API_KEY), 'utf-8')
	#r = requests.get(new_url)
	#print "Added url: ", added_url
	#print "New url: ", new_url
	r = requests.get(added_url+API_KEY)

	return jsonify(r.json())

# Running app
if __name__ == "__main__":
	app.run(debug=True)