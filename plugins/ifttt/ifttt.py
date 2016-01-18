import time
import yaml
import os.path

class ifttt(object):

	def __init__(self, config=None):

       	        print "plugin loaded"
                if config is not None and os.path.isfile(config):
                    self.config=yaml.load(file(config))
		self.SLACK_TOKEN='ABC123'

        crontable = []
        outputs = []

        def process_message(self, data):
		search_list=[data[ent] for ent in ['team', 'channel', 'user', 'text']]
		print self.getFirstAction(self.config, search_list).format('ABC123', data['user'])
                if data['channel'] == self.config['channel'] and data['user'] == self.config['user']:
			print "[{}] {}: {}".format(data['channel'], data['user'], data['text'])

	def getFirstAction(self, config_dict, search_list):
        	searching=search_list.pop(0)
        	for keydict in (config_dict[config_dict.keys()[0]]):
                	if isinstance(keydict, dict):
                        	for value in keydict.keys():
                                	if searching == value:
                                        	if keydict[value].has_key('action'):
	                                                return keydict[value]['action']
        	                                else:
							return self.getFirstAction(keydict[value], search_list)
