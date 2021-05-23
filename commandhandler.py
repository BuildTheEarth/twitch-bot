import snippethandler
from utils import Config
class CommandHandler:
	def runcommand(self, message, role):
		snippetcmd = snippethandler.SnippetHandler()
		conf = Config()
		prefix = conf.prefix()
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
