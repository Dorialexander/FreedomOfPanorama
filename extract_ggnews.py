from bs4 import BeautifulSoup
import os, codecs, re
from fuzzywuzzy import fuzz


#The parsing function to get the list of articles on google news (very rough and probably inefficient but good enough for our purposes). The output has to be copied to a csv file.
def google_article(com_dir):
	for subdir, dirs, files in os.walk(com_dir):
		for file in files:
			if file[0] != '.':
				id = re.sub(ur"panorama-(\d+)\.html", ur"\1", file, re.UNICODE)
				file = com_dir + "/" + file
				file = codecs.open(file)
				file = file.read()
				file = BeautifulSoup(file, "html.parser")
				gnews = file.findAll("div", "g")
				subdid = 0
				for gnew in gnews:
					subdid += 1
					fullid = str(id) + "-" + str(subdid)
					try:
						snippet = gnew.find('span', 'st').getText()
					except:
						snippet = "unknown"
					link = gnew.find('h3', 'r').a
					title = link.text
					if "anorama" in snippet:
						href = link['href']
						media = gnew.find('cite', '_Rm').getText()
						try:
							date = gnew.find('span', 'f').getText()
						except:
							date = "unknown"
						print(fullid + ";" + title + ";" + href + ";" + media + ";" + date)
					elif "anorama" in title:
						href = link['href']
						media = gnew.find('cite', '_Rm').getText()
						try:
							date = gnew.find('span', 'f').getText()
						except:
							date = "unknown"
						print(fullid + ";" + title + ";" + href + ";" + media + ";" + date)						
					else:
						pass
					print(fullid + ";" + title + ";" + href + ";" + media + ";" + date)


#Allow to remove the duplicates in the Google News dataset : every similar title (with fuzz ratio to take into account minor changes)
def gnew_compact_csv(csvfile, comparefile):
	file = codecs.open(csvfile)
	file = file.read()
	file = file.split('\n')
	comparefile = codecs.open(comparefile)
	comparefile = comparefile.read()
	comparefile = comparefile.lower()
	comparefile = comparefile.split('\n')
	duplicatelist = []
	for elem in file:
		try:
			title = elem.split(';')[1].lower()
			test = 0
			for comp in comparefile:
				if (fuzz.ratio(title, comp)>70):
					duplicatelist.append(elem)
		except:
			pass
	for elem in file:
		if elem not in duplicatelist:
			print(elem)
		
#Transform the collection of ggnews articles (extracted manually) into a .txt legible by iramuteq (with **** separator between text and metadata before *)
def get_ira(com_dir): 
	for subdir, dirs, files in os.walk(com_dir):
		for file in files:
			if file[0] != '.':
				filename = com_dir + "/" + file
				file = codecs.open(filename)
				file = file.read()
				file = BeautifulSoup(file, "html.parser")
				media = file.source.getText()
				media = re.sub(" \(.+?\)", "", media)
				media = re.sub(" ", "-", media)
				year = file.date.getText()
				year = re.search(ur'(?P<annee>\d\d\d\d)', str(year), re.UNICODE).group("annee")
				article = file.article.getText()
				print("**** *media_" + media + " *year_" + year + "\n\n")
				print(article)
