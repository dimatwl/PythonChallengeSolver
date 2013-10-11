__author__ = 'Dmitriy'

import urllib
from src.Solvers.Helpers.UrlParser import UrlParser

class UrlFetcher:
    def __init__(self, url_parser):
        if isinstance(url_parser, UrlParser):
            self.__url_parser = url_parser
        else:
            raise ValueError("url_parser isn't instance of UrlParser.")

    def fetch_url(self):
        return urllib.urlopen(self.__url_parser.get_url)