from flask import Flask
from parsers import Parser
from json import loads, dumps
import requests

app = Flask(__name__)

service_url_dict = {
	'google' : 'https://www.google.com/search?q=',
	'bing' : 'http://www.bing.com/search?q=',
	'yahoo' : 'https://search.yahoo.com/search?p='
}

google_parser_dict = {
	'search_result_tag' : 'li.g',
	'search_result_title_tag' : 'h3.r > a',
	'search_result_link_tag' : 'h3.r > a',
	'search_result_description_tag' : 'div.rc > div.s > div > span.st',
	'search_result_source_tag' : 'div.rc > div.s > div > div.f > div.crc > div.crl'
}

yahoo_parser_dict = {
	'search_result_tag' : 'li > div.res',
	'search_result_title_tag' : 'h3 > a',
	'search_result_link_tag' : 'span.url',
	'search_result_description_tag' : 'div.abstr',
	'search_result_source_tag' : 'span.url'
}

bing_parser_dict = {
	'search_result_tag' : 'li.b_algo',
	'search_result_title_tag' : 'h2 > a',
	'search_result_link_tag' : 'h2 > a',
	'search_result_description_tag' : 'div.b_caption > p',
	'search_result_source_tag' : 'h2 > a'
}

@app.route("/search/<service>/<query>")
def search_service(service, query):
	query_url = service_url_dict[service] + query
	html = requests.get(query_url).text
	if service == "bing":
		bing_parser = Parser(html, bing_parser_dict)
		return bing_parser.retrieve_json_data()

	elif service == "google":
		print html
		google_parser = Parser(html, google_parser_dict)
		return google_parser.retrieve_json_data()

	elif service == "yahoo":
		yahoo_parser = Parser(html, yahoo_parser_dict)
		return yahoo_parser.retrieve_json_data()

	else:
		return "Not a valid search engine: " + service

@app.route("/search/<query>")
def search_all(query):

	bing_query_url = service_url_dict['bing'] + query
	bing_html = requests.get(bing_query_url).text
	bing_parser = Parser(bing_html, bing_parser_dict)
	bing_data = loads(bing_parser.retrieve_json_data())

	google_query_url = service_url_dict['google'] + query
	google_html = requests.get(google_query_url).text
	google_parser = Parser(google_html, google_parser_dict)
	google_data = loads(google_parser.retrieve_json_data())

	yahoo_query_url = service_url_dict['yahoo'] + query
	yahoo_html = requests.get(yahoo_query_url).text
	yahoo_parser = Parser(yahoo_html, yahoo_parser_dict)
	yahoo_data = loads(yahoo_parser.retrieve_json_data())

	all_data = {
		'google' : google_data,
		'yahoo' : yahoo_data,
		'bing' : bing_data
	}

	return dumps(all_data)

if __name__ == "__main__":
    app.run(debug=True)