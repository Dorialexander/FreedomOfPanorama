# Freedom Of Panorama
This is a repository of various codes, data, and methodological notes used in a research article on Freedom of Panorama. 

## Doing text mining with Google News and Europresse

One of the main objective of this research was to track the circulation of freedom of panorama related discurses within the public sphere. Therefore, we have used a combination of text mining techniques, first experimented on XIXth century periodicals. During the past ten years, libraries have digitized newspapers archives in the public domain on a massive scale and made them increasingly available for research purposes: since december 2015, it is possible to download all the items of major European dailies in [Europeana](http://data.theeuropeanlibrary.org/download/newspapers-by-country/README.html) and, therefore, analyze wide corpora using current (correspondence analysis, word embedding) or specific (virality detection) text mining tools.

Applying the same methods to contemporary press seems apparently easier. Given the texts have always been digital, there is no issue of optical character recognition. The coverage of news aggregator appears much more extensive than that of digital libraries. We have used mainly two of these meta-sources: 
* 115 articles in English and several other languages from the result of the query "Freedom of Panorama" on Google News.
* 136 articles in French from the result of the query "Liberté de Panorama" Europresse (a proprietary database accessible through university credentials).

###Methodological difficulties (and *caveats*)

Yet, extensive does not mean comprehensive or, even, representative. We have been faced with several difficulties:

** (1) The corpora are not meant for text mining use** Europresse and Google News are mainly structured for casual human reading and not for intensive extraction. Besides, in the Google case, text mining is expressely forbidden and discouraged. For instance, we have been previously blocked as a result of a very similar project: [extracting scientific articles on Google Scholar](https://scoms.hypotheses.org/216). Several tricks allows to override this anti-bot policy such as random downloading (to make believe the extraction is processed by a humans) or regular IP renewal with tor (so that Google believes the extraction is done by several people).

<p align="center"><img src=https://github.com/Dorialexander/FreedomOfPanorama/raw/master/google_scholar.png></p>

<p align="center"><em>An efficient trick to avoid text mining blocks:<br/> using Tor to masquerade as another IP (here, assuming the identity of a polish user).</em></p>

** (2) The selection of the aggregator remains opaque**. On the whole, Europresse is more documented on regional sources that are not always well indexed on the web whereas Google News achieves a better coverage of pure player. Beyond theses leading unofficial editorial policies numerous seemingly arbitrary choices appear to be made. 

** (3) The results are not always consistent**. While we were very cautious to consult Google News in a private mode in order to avoid activating customized search processes, there were still regular variations in the size and content of the selection. Apparently, that’s a regular feature of search engines: each query can be processed by different servers; while the first pages are generally stable, the content of “deeper” pages heavily depends on the indexed database available to the targeted server. Older results seems to “disappear” from Google News : while freedom of panorama is clearly an emerging issues, we have spotted several articles published before 2015 that did not make their way.

** (4) The selection is “contaminated” by irrelevant results**. Google News frequently add texts on allegedly “close” topic, even if the expression “Freedom of Panorama” is not explicitly stated. Given the analysis is mostly stylistic, theses results have been removed from our corpora. Besides, the crawling algorithm takes the original web page as a whole, which not only include the main article but also comments and news feeds. 

###A methodological twist: Google News represents itself!

On most of theses methodological aspects, Europresse fares better than Google News. Yet, Google News still has a significant advantage: it is actually read by millions of europeans, who use the aggregator as their prime portal to media and view the evolving news agenda from theses (somewhat distorted) lenses. If there's a leading (rather than comprehensive) panorama of the public sphere debate surrounding Freedom of panorama it is undisputedly on Google News. This de facto concentration of news reading practices has stirred numerous economic and legal debate. The June 2016 EU consultation on Freedom of panorama was therefore paired with a consultation on granting neighboring rights to publishers and, possibly, restraining secondary providers the right to link or to quote news.

Therefore, each corpus will be considered on different ground. While Europresse maps not so imperfectly the general dynamics of French news, Google News is chiefly representative of Google News (that is of the main digital platform through which readers discover news). Paradoxically enough, even in this tautological approach, Google News is not completely reliable: as we showed it previously, results change and disappear from time to time and are potentially generated in a different way from one consultation to another. All theses biases remain nevertheless far more limited than if we used Google News as a valid representation of all news.

##Extracting the articles

###The extraction process of Google News.

All the result pages (in html) of the query "freedom of panorama" were registered locally. Several parsing functions then allowed to transform the html structure as a dataset of links, article title, date and media name. In the same manneer we have removed some duplicated results (by checking if a title were already in the dataset). Some time, Google News issued results that did not includ the proper name "freedom of panorama" and usually talked about a different topic (albeit somewhat linked). We have consequently removed every result that did not mention the expression "freedom of panorama" in the snippets. The initial corpora of almost 160 articles were therefore reduced by about one fourth to 115 articles.
