# Freedom Of Panorama Supplementary Data Paper
This is a repository of various codes, data, and methodological notes used in a research article on Freedom of Panorama. 

## Doing text mining with Google News and Europresse

One of the main objective of this research was to track the circulation of freedom of panorama related discurses within the public sphere. Therefore, we have used a combination of text mining techniques, first experimented on XIXth century periodicals. During the past ten years, libraries have digitized newspapers archives in the public domain on a massive scale and made them increasingly available for research purposes: since december 2015, it is possible to download all the items of major European dailies in [Europeana](http://data.theeuropeanlibrary.org/download/newspapers-by-country/README.html) and, therefore, analyze wide corpora using current (correspondence analysis, word embedding) or specific (virality detection) text mining tools.

Applying the same methods to contemporary press seems apparently easier. Given the texts have always been digital, there is no issue of optical character recognition. The coverage of news aggregator appears much more extensive than that of digital libraries. We have used mainly two of these meta-sources: 
* 115 articles in English and several other languages from the result of the query "Freedom of Panorama" on Google News.
* 136 articles in French from the result of the query "Liberté de Panorama" Europresse (a proprietary database accessible through university credentials).

###Methodological difficulties (and *caveats*)

Yet, extensive does not mean comprehensive or, even, representative. We have been faced with several difficulties:

* **(1) The corpora are not meant for text mining use.** Europresse and Google News are mainly structured for casual human reading and not for intensive extraction. Besides, in the Google case, text mining is expressely forbidden and discouraged. For instance, we have been previously blocked as a result of a very similar project: [extracting scientific articles on Google Scholar](https://scoms.hypotheses.org/216). Several tricks allows to override this anti-bot policy such as random downloading (to make believe the extraction is processed by a humans) or regular IP renewal with tor (so that Google believes the extraction is done by several people).

<p align="center"><img src=https://github.com/Dorialexander/FreedomOfPanorama/raw/master/google_scholar.png></p>

<p align="center"><em>An efficient trick to avoid text mining blocks:<br/> using Tor to masquerade as another IP (here, assuming the identity of a polish user).</em></p>

* **(2) The selection of the aggregator remains opaque**. On the whole, Europresse is more documented on regional sources that are not always well indexed on the web whereas Google News achieves a better coverage of pure player. Beyond theses leading unofficial editorial policies numerous seemingly arbitrary choices appear to be made. 

* **(3) The results are not always consistent**. While we were very cautious to consult Google News in a private mode in order to avoid activating customized search processes, there were still regular variations in the size and content of the selection. Apparently, that’s a regular feature of search engines: each query can be processed by different servers; while the first pages are generally stable, the content of “deeper” pages heavily depends on the indexed database available to the targeted server. Older results seems to “disappear” from Google News : while freedom of panorama is clearly an emerging issues, we have spotted several articles published before 2015 that did not make their way.

* **(4) The selection is “contaminated” by irrelevant results**. Google News frequently add texts on allegedly “close” topic, even if the expression “Freedom of Panorama” is not explicitly stated. Given the analysis is mostly stylistic, theses results have been removed from our corpora. Besides, the crawling algorithm takes the original web page as a whole, which not only include the main article but also comments and news feeds. 

###A methodological twist: Google News represents itself!

On most of theses methodological aspects, Europresse fares better than Google News. Yet, Google News still has a significant advantage: it is actually read by millions of europeans, who use the aggregator as their prime portal to media and view the evolving news agenda from theses (somewhat distorted) lenses. If there's a leading (rather than comprehensive) panorama of the public sphere debate surrounding Freedom of panorama it is undisputedly on Google News. This de facto concentration of news reading practices has stirred numerous economic and legal debate. The June 2016 EU consultation on Freedom of panorama was therefore paired with a consultation on granting neighboring rights to publishers and, possibly, restraining secondary providers the right to link or to quote news.

Therefore, each corpus will be considered on different ground. While Europresse maps not so imperfectly the general dynamics of French news, Google News is chiefly representative of Google News (that is of the main digital platform through which readers discover news). Paradoxically enough, even in this tautological approach, Google News is not completely reliable: as we showed it previously, results change and disappear from time to time and are potentially generated in a different way from one consultation to another. All theses biases remain nevertheless far more limited than if we used Google News as a valid representation of all news.

##Mining the articles

###Google News.

All the result pages (in html) of the query "freedom of panorama" were registered locally. Several parsing functions (within [extract_ggnews.py](https://github.com/Dorialexander/FreedomOfPanorama/blob/master/extract_ggnews.py)) then allowed to transform the html structure as a dataset of links, article title, date and media name. Some time, Google News issued results that did not includ the proper name "freedom of panorama" and usually talked about a different topic (albeit somewhat linked). We have consequently removed every result that did not mention the expression "panorama" in the snippets. 

```python
#"anorama" rather than panorama as a lazy way to avoid taking caps into account…
if "anorama" in snippet:
	href = link['href']
	media = gnew.find('cite', '_Rm').getText()
	try:
		date = gnew.find('span', 'f').getText()
	except:
		date = "unknown"
	print(fullid + ";" + title + ";" + href + ";" + media + ";" + date)
```

In the same manneer we have removed some duplicated results by checking if a title were already in the dataset. We used a "fuzzy" match rather than a strict string comparison to take into account small variations (for instance regarding punctuations).

```python
for elem in file:
	try:
		title = elem.split(';')[1].lower()
		test = 0
		for comp in comparefile:
			if (fuzz.ratio(title, comp)>70):
				duplicatelist.append(elem)
	except:
		pass
```

The initial corpus of almost 160 articles was therefore reduced by about one fourth to 115 articles to create the dataset "[gg_news_all_language.csv](https://github.com/Dorialexander/FreedomOfPanorama/blob/master/ggnews_all_languages.csv)".

The articles were then extracted on a copy-paste method. Unfortunately the wide variability of html use accross the newspapers prevented using efficient automated parsing (which would have really paid off on a much larger corpus). Each article was classed by language. While the high diversity of our corpus was a significant piece of information, we focused our textual analysis on the 67 English articles (listed in "[gg_news_en.csv](https://github.com/Dorialexander/FreedomOfPanorama/blob/master/gg_news_en.csv)"). Reproducing the cleaned corpus would be at loss with existing EU copyright laws: while all theses articles are "free to read", they are not "free to copy". For replication purposes, it should still be possible to reconstruct our collection using the list of link.

###Europresse

Europresse is easier to use for text mining purposes : the actual text is already separated from its original editorial context. Besides, the coverage is both wider and more stable than on Google News (as it even seems to aggregate sources that are not accessible online). Nevertheless, the proprietary nature of the database and its accessibility focused on French universities greatly limits its replicative value.

All the HTML files of the articles of Europresse were saved locally. The function "ira_article" in  "[extract_europresse.py](https://github.com/Dorialexander/FreedomOfPanorama/blob/master/extract_europresse.py)" allows a direct transformation of HTML to the txt format used by iramuteq.

##Analyzing the articles

###Iramuteq

[Iramuteq](http://www.iramuteq.org/) is a free interface of the R langage for textual analysis. It offers an efficient pipelpine for existing R functions (in library such as [TM](https://cran.r-project.org/web/packages/tm/index.html), [CA](https://cran.r-project.org/web/packages/ca/ca.pdf), [igraph](http://igraph.org/r/)…) and implement some original methods (Reinert classification, similarity networks). Our use of Iramuteq was very straightforward: we ran the Reinert classification with the default settings (unsupervised training on segments of 40 words), which were fine for our limited sample but could stress standard hardware on wider corpus (we had actually meet this problem on an unrelated project dealing with several hundred pieces of litterature). Iramuteq then produces a set of visual and data files in a directory. The picture, below, is the standard correspondence analysis on the Google News corpus with the colors mapping the class identified by the Reinert method.

<p align="center"><img src=https://github.com/Dorialexander/FreedomOfPanorama/raw/master/AFC2DL.png width="320px"></p>

###R

While the Iramuteq standard visualization were quite informative during the analyzes process, they do not render so well for publication purposes. For instances, the words are too numerous (and, consequently, too small). In order to avoid overlap, coordinates are altered (which may result, sometimes, in slightly inaccurate representation of proximity from word to another). Finally, Iramuteq also produces a correspondence analysis of variable (either "year" ou "media" in our case) but keeps the name of the variable as a prefix. This disposition greatly complicates the reading while it could be much more efficient to focuse the dataviz on only one variable.




