import snippethandler
from utils import Config
import re

class CommandHandler:
	def __init__(self):
		self.regexLink = re.compile(r"""https?:\/\/(?!clips.twitch.tv)[^./]+(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)""")
	def runcommand(self, message, role, messageID):
		if not ("moderator" in role or "broadcaster" in role or "subscriber" in role):
			if self.regexLink.search(message) != None:
				return f"/delete {messageID}"
			
		snippetcmd = snippethandler.SnippetHandler()
		conf = Config()
		prefix = conf.prefix
		prefixlen = len(prefix)-1
		if message[prefixlen] == prefix:
			tempthing = message.lstrip(prefix).split(" ")
			if len(tempthing) >= 4:
				tempthing.pop(0)
				tempthing.pop(0)
				tempthing.pop(0)
				tempthing.pop(0)
			tempstr = " "
			tempstr = tempstr.join(tempthing)
			if message.lstrip(prefix).split(" ")[0] == "snippets":
				if len(message.lstrip(prefix).split(" ")) == 1:
					return snippetcmd.listwithlangs()
				if message.lstrip(prefix).split(" ")[1] == "language":
					if (len(message.lstrip(prefix).split(" ")) >= 3) == False:
						return "Not enough arguments provided. Usage: " + prefix + "snippets language <name>"
					else:
						return snippetcmd.getlanglist(message.lstrip(prefix).split(" ")[2])
				if message.lstrip(prefix).split(" ")[1] == "add":
					if "moderator" in role or "broadcaster" in role:
						if (len(message.lstrip(prefix).split(" ")) >= 5) == False:
							return "Not enough arguments provided"
						else:
							return snippetcmd.add(message.lstrip(prefix).split(" ")[2], tempstr, message.lstrip(prefix).split(" ")[3])
				if message.lstrip(prefix).split(" ")[1] == "edit":
					if "moderator" in role or "broadcaster" in role:
						if (len(message.lstrip(prefix).split(" ")) >= 5) == False:
							return "Not enough arguments provided"
						else:
							return snippetcmd.edit(message.lstrip(prefix).split(" ")[2], tempstr, message.lstrip(prefix).split(" ")[3])

				if message.lstrip(prefix).split(" ")[1] == "delete":
					if "moderator" in role or "broadcaster" in role:
						if (len(message.lstrip(prefix).split(" ")) >= 4) == False:
							return "Not enough arguments provided"
						else:
							return snippetcmd.delete(message.lstrip(prefix).split(" ")[2], message.lstrip(prefix).split(" ")[3])
			elif len(message.lstrip(prefix).split(" ")) == 1:
				if snippetcmd.get(message.lstrip(prefix).split(" ")[0], "en") != False:
					return snippetcmd.get(message.lstrip(prefix).split(" ")[0], "en")
			elif len(message.lstrip(prefix).split(" ")) >= 2:
				if snippetcmd.get(message.lstrip(prefix).split(" ")[0], message.lstrip(prefix).split(" ")[1]) != False:
					return snippetcmd.get(message.lstrip(prefix).split(" ")[0], message.lstrip(prefix).split(" ")[1])
