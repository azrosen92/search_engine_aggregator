from bs4 import BeautifulSoup
from json import dumps

class Parser():
	def __init__(self, html, parser_dict):
		self.dom = BeautifulSoup(html)
		self.parser_dict = parser_dict

	def retrieve_json_data(self):
		result_objects = []

		for result in self.dom.select(self.parser_dict['search_result_tag']):
			search_result_title = None
			search_result_link = None
			search_result_description = None
			search_result_source = None

			print result.select(self.parser_dict['search_result_description_tag'])

			if result.select(self.parser_dict['search_result_title_tag']):
				search_result_title = result.select(self.parser_dict['search_result_title_tag'])[0].decode_contents(formatter="html")
				print "Search result title: ", search_result_title
			if result.select(self.parser_dict['search_result_link_tag']):
				search_result_link = result.select(self.parser_dict['search_result_link_tag'])[0].get("href")
				print "Search result link: ", search_result_link
			if result.select(self.parser_dict['search_result_description_tag']):
				search_result_description = result.select(self.parser_dict['search_result_description_tag'])[0].decode_contents(formatter="html")
				print "Search result description: ", search_result_description
			if result.select(self.parser_dict['search_result_source_tag']):
				search_result_source = result.select(self.parser_dict['search_result_source_tag'])[0].decode_contents(formatter="html")
				print "Search result source: ", search_result_source

			print "----------------------------------------------"

			# Add to list of result objects.
			result_objects.append(
				{'search_result_title' : search_result_title,
				 'search_result_link' : search_result_link,
				 'search_result_description' : search_result_description,
				 'search_result_source' : search_result_source})

		# Construct JSON object with above infomation.
		return dumps(result_objects)