import textwrap
from utils import Config
from isolanghandler import isolang
from sqlalchemy import create_engine
from sqlalchemy import text
import urllib.parse
class SnippetHandler:
#CREATE TABLE snippets (name text, content text, lang text);

	def __init__(self):
		conf = Config()
		self.prefix = conf.prefix
		self.engine = create_engine(conf.db_url, future=True)

	def listwithlangs(self): # return a dict of snippets
		res = {}
		with self.engine.connect() as database:
			for snippet in database.execute(text("SELECT * FROM snippets ORDER BY name")):
				if (self.prefix + snippet[0]) not in res:
					res[self.prefix + snippet[0]] = []
					res[self.prefix + snippet[0]].append(snippet[2])
				else:
					res[self.prefix + snippet[0]].append(snippet[2])
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
		with self.engine.connect() as database:
			for snippetcheck in database.execute(text("select * from snippets where name=:name"),{"name": name}):
				moveon = True
		if moveon == False:
			return "Invalid Snippet"
		with self.engine.connect() as database:
			for snippet in database.execute(text("SELECT * FROM snippets ORDER BY name")):
				if (self.prefix + snippet[0]) not in res:
					res[self.prefix + snippet[0]] = []
					res[self.prefix + snippet[0]].append(snippet[2])
				else:
					res[self.prefix + snippet[0]].append(snippet[2])
		if format == True:
			for key in res.keys():
				splitter = ", "
				res[key] = str(" Languages: "+splitter.join(res[key])+ ".")
		return res["=" + name]

	def list(self): # return a dict of snippets
		res = {}
		with self.engine.connect() as database:
			for snippet in database.execute(text('SELECT * FROM snippets ORDER BY name')):
        			res[snippet[0]] = snippet[1]

		return res
	def add(self, name, content, lang): #add snippet
		if name == "snippets":
			return "Hey silly, dont try making a snippet of a command name"
		langcheck = isolang()
		name = name.lower()
		lang = lang.lower()
		if langcheck.isvalid(lang) == False:
			return "Invalid Language"
		with self.engine.connect() as database:
			for snippets in database.execute(text("select * from snippets where name=:name and lang=:lang"),{"name": name, "lang": lang}):
				if (snippets[0] == name) and (snippets[2] == lang):
					database.commit()
					return "Snippet Already Exists, use " + self.prefix + "snippets edit to edit it"
			database.execute(text("insert into snippets values (:name, :content, :lang)"), {"name": name, "content": content, "lang": lang})
			database.commit()
		return f'Snippet {name} has been sucessfully added in {langcheck.langname(lang)}'
	def edit(self, name, content, lang): #edit
		langcheck = isolang()
		name = name.lower()
		lang = lang.lower()
		if langcheck.isvalid(lang) == False:
			return "Invalid Language"
		with self.engine.connect() as database:
			for snippets in database.execute(text("select * from snippets where name=:name and lang=:lang"),{"name": name, "lang": lang}):
				if (snippets[0] == name) and (snippets[2] == lang):
					database.execute(text("delete from snippets where name=:name and lang=:lang"),{"name": name, "lang": lang})
					database.execute(text("insert into snippets values (:name, :content, :lang)"), {"name": name, "content": content, "lang": lang})
					database.commit()
					return f"Snippet {name} has been sucessfully edited in {langcheck.langname(lang)}"
			database.commit()
		return "Snippet dosent exist, use " + self.prefix + "snippets add to add it"
	def get(self, name, lang):
		langcheck = isolang()
		name = name.lower()
		lang = lang.lower()
		if langcheck.isvalid(lang) == False:
			return False
		with self.engine.connect() as database:
			for snippets in database.execute(text("select * from snippets where name=:name and lang=:lang"),{"name": name, "lang": lang}):
				return snippets[1]
		return False
	def delete(self, name, lang):
		langcheck = isolang()
		name = name.lower()
		lang = lang.lower()
		if langcheck.isvalid(lang) == False:
			return "Invalid Language"
		with self.engine.connect() as database:
			for snippets in database.execute(text("select * from snippets where name=:name and lang=:lang"),{"name": name, "lang": lang}):
				if (snippets[0] == name) and (snippets[2] == lang):
					database.execute(text("delete from snippets where name=:name and lang=:lang"),{"name": name, "lang": lang})
					database.commit()
					return f"Snippet {name} has been sucessfully deleted in {langcheck.langname(lang)}"
			database.commit()
		return "You cant delete a snippet that dosent exist. Silly"
