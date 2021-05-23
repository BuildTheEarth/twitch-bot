import sqlite3
import textwrap
from utils import Config
from isolanghandler import isolang
from sqlalchemy import create_engine
class SnippetHandler:
#snippet create is CREATE TABLE snippets (name text, content text, lang text);

	def __init__(self):
		conf = Config()
		self.prefix = conf.prefix()
		self.engine = create_engine(conf.db_url(), echo=True, future=True)

	def listwithlangs(self): # return a dict of snippets
		res = {}
		connection = sqlite3.connect('snippets.db')
		database = connection.cursor()
		for snippet in database.execute('SELECT * FROM snippets ORDER BY name'):
			if (self.prefix + snippet[0]) not in res:
				res[self.prefix + snippet[0]] = []
				res[self.prefix + snippet[0]].append(snippet[2])
			else:
        			res[self.prefix + snippet[0]].append(snippet[2])
		connection.close()
		returnstr = "Snippets: "
		for key in res.keys():
			splitter = " | "
			if res[key] == ["en"]:
				res[key] = ""
			else:
				res[key] = str(" <"+splitter.join(res[key])+ ">")
		for key in res.keys():
			returnstr = returnstr + key +  ", "
		returnstr = returnstr.rstrip(", ") + ". To find which languages a snippet has available, you can do " + self.prefix + "snippets language <name of snippet>"
		if len(returnstr) > 470:
			return textwrap.fill(returnstr, 470).split("\n")
		return returnstr

	def getlanglist(self, name, format = True): # return a dict of snippets
		res = {}
		name = name.lower()
		moveon = False
		connection = sqlite3.connect('snippets.db')
		database = connection.cursor()
		for snippetcheck in database.execute("select * from snippets where name=:name",{"name": name}):
			moveon = True
		if moveon == False:
			return "Invalid Snippet"
		for snippet in database.execute('SELECT * FROM snippets ORDER BY name'):
			if (self.prefix + snippet[0]) not in res:
				res[self.prefix + snippet[0]] = []
				res[self.prefix + snippet[0]].append(snippet[2])
			else:
        			res[self.prefix + snippet[0]].append(snippet[2])
		if format == True:
			for key in res.keys():
				splitter = ", "
				res[key] = str(" Languages: "+splitter.join(res[key])+ ".")
		connection.close()
		return res["=" + name]

	def list(self): # return a dict of snippets
		res = {}
		connection = sqlite3.connect('snippets.db')
		database = connection.cursor()
		for snippet in database.execute('SELECT * FROM snippets ORDER BY name'):
        		res[snippet[0]] = snippet[1]
		connection.close()

		return res
	def add(self, name, content, lang): #add snippet
		if name == "snippets":
			return "Hey silly, dont try making a snippet of a command name"
		langcheck = isolang()
		name = name.lower()
		lang = lang.lower()
		if langcheck.isvalid(lang) == False:
			return "Invalid Language"
		connection = sqlite3.connect('snippets.db')
		database = connection.cursor()
		for snippets in database.execute("select * from snippets where name=:name and lang=:lang",{"name": name, "lang": lang}):
			if (snippets[0] == name) and (snippets[2] == lang):
				connection.commit()
				connection.close()
				return "Snippet Already Exists, use " + self.prefix + "snippets edit to edit it"
		database.execute("insert into snippets values (?, ?, ?)", (name, content, lang))
		connection.commit()
		connection.close()
		return f'Snippet {name} has been sucessfully added in {langcheck.langname(lang)}'
	def edit(self, name, content, lang): #edit
		langcheck = isolang()
		name = name.lower()
		lang = lang.lower()
		if langcheck.isvalid(lang) == False:
			return "Invalid Language"
		connection = sqlite3.connect('snippets.db')
		database = connection.cursor()
		for snippets in database.execute("select * from snippets where name=:name and lang=:lang",{"name": name, "lang": lang}):
			if (snippets[0] == name) and (snippets[2] == lang):
				database.execute("delete from snippets where name=:name and lang=:lang",{"name": name, "lang": lang})
				database.execute("insert into snippets values (?, ?, ?)", (name, content, lang))
				connection.commit()
				connection.close()
				return f"Snippet {name} has been sucessfully edited in {langcheck.langname(lang)}"
		connection.commit()
		connection.close()
		return "Snippet dosent exist, use " + self.prefix + "snippets add to add it"
	def get(self, name, lang):
		langcheck = isolang()
		name = name.lower()
		lang = lang.lower()
		if langcheck.isvalid(lang) == False:
			return False
		connection = sqlite3.connect('snippets.db')
		database = connection.cursor()
		for snippets in database.execute("select * from snippets where name=:name and lang=:lang",{"name": name, "lang": lang}):
			return snippets[1]


		connection.commit()
		connection.close()
		return False
	def delete(self, name, lang):
		langcheck = isolang()
		name = name.lower()
		lang = lang.lower()
		if langcheck.isvalid(lang) == False:
			return "Invalid Language"
		connection = sqlite3.connect('snippets.db')
		database = connection.cursor()
		for snippets in database.execute("select * from snippets where name=:name and lang=:lang",{"name": name, "lang": lang}):
			if (snippets[0] == name) and (snippets[2] == lang):
				database.execute("delete from snippets where name=:name and lang=:lang",{"name": name, "lang": lang})
				connection.commit()
				connection.close()
				return f"Snippet {name} has been sucessfully deleted in {langcheck.langname(lang)}"
		connection.commit()
		connection.close()
		return "You cant delete a snippet that dosent exist. Silly"
