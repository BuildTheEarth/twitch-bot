import json
from irc.bot import SingleServerIRCBot
from requests import get
import commandhandler

with open("config.json") as e:
	conf = json.load(e)
	TOKEN = conf['token']
	CLIENT_ID = conf['client_id']
	NAME = conf['username']
	OWNER = conf['channel']
	PREFIX = conf['prefix']
	DB_URL = conf['db_url']
	if bool(TOKEN):
		if isinstance(TOKEN, str) == False:
			print("token must be a string")
			quit()
	elif bool(CLIENT_ID):
		if isinstance(CLIENT_ID, str) == False:
			print("client_id must be a string")
			quit()
	elif bool(OWNER):
		if isinstance(TOKEN, str) == False:
			print("channel must be a string")
			quit()
	elif bool(NAME):
		if isinstance(TOKEN, str) == False:
			print("username must be a string")
			quit()
	elif bool(PREFIX):
		if isinstance(TOKEN, str) == False:
			print("prefix must be a string")
			quit()
	elif bool(PREFIX):
		if isinstance(TOKEN, str) == False:
			print("db_url must be a string")
			quit()
	else:
		print("please fill out your config")
		quit()


class Bot(SingleServerIRCBot):
	def __init__(self):
		self.COMMAND = commandhandler.CommandHandler()
		self.HOST = "irc.chat.twitch.tv"
		self.PORT = 6667
		self.USERNAME = NAME.lower()
		self.CLIENT_ID = CLIENT_ID
		self.TOKEN = TOKEN
		self.CHANNEL = f"#{OWNER}"

		url = f"https://api.twitch.tv/kraken/users?login={self.USERNAME}"
		headers = {"Client-ID": self.CLIENT_ID, "Accept": "application/vnd.twitchtv.v5+json"}
		resp = get(url, headers=headers).json()
		self.channel_id = resp["users"][0]["_id"]

		super().__init__([(self.HOST, self.PORT, f"oauth:{self.TOKEN}")], self.USERNAME, self.USERNAME)

	def on_welcome(self, cxn, event):
		for req in ("membership", "tags", "commands"):
			cxn.cap("REQ", f":twitch.tv/{req}")

		cxn.join(self.CHANNEL)
		print("Started")


	def on_pubmsg(self, cxn, event):
		tags = {kvpair["key"]: kvpair["value"] for kvpair in event.tags}
		user = {"name": tags["display-name"], "id": tags["user-id"]}
		message = event.arguments[0]
		if event.tags[1]['value'] != None:
			role = event.tags[1]['value']
		else:
			role = ""
		messageID = event.tags[7]['value']
		reply = self.COMMAND.runcommand(message, role, messageID)
		if bool(reply):
			if isinstance(reply, list):
				for msg in reply:
					self.send_message(msg)
			else:
				self.send_message(reply)
	def send_message(self, message):
		self.connection.privmsg(self.CHANNEL, message)

	def ban_user(self, username):
		self.send_message(f"/ban {username}")

	def timeout_user(self, username, seconds):
		self.send_message(f"/timeout {username}")

	def unpunish_user(self, username):
		self.send_message(f"/unban {username}")

if __name__ == "__main__":
	bot = Bot()
	bot.start()