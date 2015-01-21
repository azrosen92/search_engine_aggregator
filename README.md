Ebay Coding Challenge - Search Engine Aggregator
================================================

To start application run `~$ python parser_api.py`

Depends on:
- Flask
- requests
- beautifulsoup

Routes
-------
**/search/:service/:query** Returns results for a search of :query in the
:service search engine.

**/search/:query** Returns results for a search of :query in all search engines.

Reponses
---------
**JSON data format**

	[{
		'search_result_title',
		'search_result_link',
		'search_result_description',
		'search_result_source'
	}]

I had a problem with the html I was receiving from Google search results, 
they did not parse correctly and the search_result_description and
search_result_source field is empty for all results. So I've included the
file google.html which is the html from a google search of the term "hurricane"
copy/pasted into a document which is parsed by the same class used in 
my api, but I get results for all of the fields.

