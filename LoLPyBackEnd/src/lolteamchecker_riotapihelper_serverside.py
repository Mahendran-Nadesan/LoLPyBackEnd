'''
LoLTeamCheckerServerSide

Provides a wrapper for the LoLTeamChecker app at
http://mahennads.pythonanywhere.com/ '''

import urlparse
from riotapipy import *
from constants import *

class lolteamchecker_riotapihelper_serverside:
	'''Parses args from LoLTeamChecker client-side urls and prepares them for the RiotAPI. URLs should be sent in the form /{region}/{stat_type}/{arg_val}
	'''
	def __init__(self, *argv):
		'''Initialises url parser'''
		self.args = {}
		keys = ['region', 'stat_types', 'arg_val']
		#self.args['all'] = urlparse.urlparse(url).path
		for i, arg in enumerate(argv):
			self.args[keys[i]] = arg
		self.api_instance = RiotApiPy(API_KEY, VERSIONS, self.args['region'])

	def get_data(self):
		'''Makes the url for the Riot servers.'''
		if self.args['stat_types'] == 'summoner':
			self.data = self.api_instance.get_summoners_by_name(self.args['arg_val'].encode('utf-8'), self.args['region'])
		if self.args['stat_types'] == 'ranked':
			self.data = self.api_instance.get_ranked_stats_by_summoner_id(self.args['arg_val'], SEASON)
		if self.args['stat_types'] == 'champion':
			self.data = self.api_instance.static_get_champion_list()
		return self.data


		#get summoners by name
		#get ranked stats by summoner id
		#static get champion list
