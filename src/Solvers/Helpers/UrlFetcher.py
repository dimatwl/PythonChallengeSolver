__author__ = 'Dmitriy'

import urllib.request
from src.Solvers.Helpers.UrlParser import UrlParser

class UrlFetcher:
    def __init__(self, url_parser):
        if isinstance(url_parser, UrlParser):
            self.__url_parser = url_parser
        else:
            raise ValueError("url_parser isn't instance of UrlParser.")

    def fetch_url(self):
        request = urllib.request.Request(self.__url_parser.get_url())
        response = urllib.request.urlopen(request)
        page_code = response.read()
        return page_code