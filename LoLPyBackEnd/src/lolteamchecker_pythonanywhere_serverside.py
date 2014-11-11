'''
LoLPyBackEnd for http://mahennads.pythonanywhere.com/
'''

# imports
import flask
from lolteamchecker_riotapihelper_serverside import *

# Set up flask app
app = flask.Flask(__name__)

# Constants

@app.route('/<path:region>/<path:stat_type>/<path:arg_val>')
def redirect(region, stat_type, arg_val):
	'''Redirect to the Riot servers with arguments.'''
	server_data = lolteamchecker_riotapihelper_serverside(region, stat_type, arg_val)
	server_data.get_data()
	return flask.jsonify(server_data.data)

@app.route('/<path:region>/<path:stat_type>')
def static_redirect(region, stat_type):
	'''Redirect without arguments.'''
	server_data = lolteamchecker_riotapihelper_serverside(region, stat_type)
	server_data.get_data()
	return flask.jsonify(server_data.data)

# Running app
# comment out everything below when on pythonanywhere
if __name__ == "__main__":
	app.run(debug=True)
