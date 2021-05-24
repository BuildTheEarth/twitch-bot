import json
class Config:
	def __init__(self):
		with open("config.json") as e:
			conf = json.load(e)
			self.prefix = conf['prefix']
			self.db_url = conf['db_url']
	def prefix(self):
		return self.prefix
	def db_url(self):
		return self.db_url
