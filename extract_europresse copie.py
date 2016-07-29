from bs4 import BeautifulSoup
import os, codecs, re
from fuzzywuzzy import fuzz


def ira_article(com_dir):
	for subdir, dirs, files in os.walk(com_dir):
		for file in files:
			if file[0] != '.':
				file = com_dir + "/" + file
				file = codecs.open(file)
				file = file.read()
				file = BeautifulSoup(file, "html.parser")
				file = file.find("div", {"id": "docText"}).article
				header = file.header
				content = file.section.div.div.getText() 
				title = header.findAll('div', 'titreArticle')[0]
				try:
					author = header.findAll('div', 'docAuthors')[0].getText()
				except:
					author = "unknown"
				codemedia = header.img['sourcecode']
				docheader = header.findAll('span', 'DocHeader')[0]
				date = re.search(ur'\d+ .+? \d+', str(docheader), re.UNICODE).group(0)
				annee = re.search(ur'\d+ .+? (?P<annee>\d+)', str(docheader), re.UNICODE).group("annee")
				try:
					media = header.findAll('span', 'DocPublicationName')[0].getText()
				except:
					media = "unknown"
				try:
					irahead = "****" + " *media_" + codemedia + " *annee_" + annee
					print(irahead)
					print(content)
				except:
					pass

ira_article("dir")
