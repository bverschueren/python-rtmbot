#!/usr/bin/env python

import time
import yaml
import os.path
import requests
import copy

class ifttt(object):

	def __init__(self, config=None):
                if config is not None and os.path.isfile(config):
                    self.config=yaml.load(file(config))
		    self.SLACK_TOKEN=self.config['SLACK_TOKEN']

        crontable = [] # might be checked by calling class
        outputs = [] # might be checked by calling class

        def process_message(self, data):
		search_list=[data[ent] for ent in ['team', 'channel', 'user', 'text']]
		action_dict=self.getFirstAction(self.config['team'], search_list)
		if action_dict is not None:
			action = action_dict['url'] + action_dict['chain'].pop(0) + '?' 
			for param in action_dict['extra_params']:
				action += param
			post_data=data.copy()
			post_data.update(action_dict)
			post_data.update({"reply_with": self.SLACK_TOKEN, "email": self.getUserEmailFromId(data['user']), "username": self.getUserNameFromId(data['user'])})
			print requests.post(action, params=post_data).text

	def getFirstAction(self, config_dict, search_list):
        	searching=search_list.pop(0)
        	for subdict in (config_dict):
                	if isinstance(subdict, dict):
                        	for key in subdict.keys():
                                	if searching == key:
                                        	if subdict[key].has_key('action'):
	                                                return copy.deepcopy(subdict[key]['action'])
        	                                else:
							return self.getFirstAction(subdict[key][subdict[key].keys()[0]], search_list)
			else:
				return None	

	def getUserEmailFromId(self, user_id):
		return requests.get('https://slack.com/api/users.info', params={'token': self.SLACK_TOKEN, 'user': user_id}).json()['user']['profile']['email']

	def getUserNameFromId(self, user_id):
                return requests.get('https://slack.com/api/users.info', params={'token': self.SLACK_TOKEN, 'user': user_id}).json()['user']['name']

