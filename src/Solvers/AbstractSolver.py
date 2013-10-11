__author__ = 'DimaTWL'

from abc import ABCMeta
from abc import abstractmethod
from src.Solvers.Helpers.UrlParser import UrlParser
from src.Solvers.Helpers.UrlFetcher import UrlFetcher

class AbstractSolver:
    __metaclass__ = ABCMeta

    def __init__(self, base_url):
        self.__valid_url_scheme = "http"
        self.__valid_url_hostname = "www.pythonchallenge.com"
        self.__url_helper = UrlParser(base_url, self.__valid_url_scheme, self.__valid_url_hostname)
        self.__url_fetcher = UrlFetcher(self.__url_helper)
        self.__base_url = base_url
        self.__next_url = None

    def get_next_url(self):
        self.__next_url = self.solve()
        return self.__next_url

    def get_url_parser(self):
        return self.__url_helper

    def get_url_fetcher(self):
        return self.__url_fetcher

    def __get_base_url(self):
        return self.__base_url

    """This method should return next URL"""
    @abstractmethod
    def solve(self):
        raise NotImplementedError("Trying to call solve in AbstractSolver.")