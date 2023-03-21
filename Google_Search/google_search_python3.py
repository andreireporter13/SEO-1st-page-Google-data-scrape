#
#
#
# Google Search Scraper ---> 
#
#
#
# Python module for search in Google
from googlesearch import search
#
#
#
class GoogleSearch:
    """
    Python class for searching in Google. 
    This script can make simple, with functions... but I want to learn OOP.
    """

    def __init__(self, keyword_search: str, num_result=5, lang='ro'):
        self.keyword_search = keyword_search
        self.lang = lang
        self.num_result = num_result

        # list with links from Google
        self.list_with_links_from_google = []

    
    def search_by_keyword(self):
        """ 
        This method search in Google by keyword.
        """

        data = search(self.keyword_search, self.num_result, self.lang)
        
        for link in data: 
            self.list_with_links_from_google.append(link)

        return self.list_with_links_from_google
