from parsers import Parser

html = open('google.html', 'r').read()

google_parser_dict = {
	'search_result_tag' : 'li.g',
	'search_result_title_tag' : 'h3.r > a',
	'search_result_link_tag' : 'h3.r > a',
	'search_result_description_tag' : 'div.s > div > span.st',
	'search_result_source_tag' : 'div.s > div > div.f > div.crc > div.crl'
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

google_parser = Parser(html, google_parser_dict)
yahoo_parser = Parser(html, yahoo_parser_dict)
bing_parser = Parser(html, bing_parser_dict)

pp = PrettyPrinter(indent=4)

print google_parser.retrieve_json_data()

