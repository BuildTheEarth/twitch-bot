class Config:
	def __init__(self):
		with open("config.json") as e:
			conf = json.load(e)
			this.prefix = conf['prefix']
			this.db_url = conf['db_url']
	def prefix(self):
		return this.prefix
	def db_url(self):
		return this.db_url
