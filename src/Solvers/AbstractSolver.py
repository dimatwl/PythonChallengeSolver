__author__ = 'DimaTWL'

from abc import ABCMeta
from abc import abstractmethod

from src.Solvers.UrlParser import UrlParser


class AbstractSolver:
    __metaclass__ = ABCMeta

    def __init__(self, base_url):
        self.__valid_url_scheme = "http"
        self.__valid_url_hostname = "www.pythonchallenge.com"
        self.__url_helper = UrlParser(base_url, self.__valid_url_scheme, self.__valid_url_hostname)
        self.__base_url = base_url
        self.__next_url = None

    def get_next_url(self):
        self.__next_url = self.__solve()
        return self.__next_url

    def get_url_parser(self):
        return self.__url_helper

    def __get_base_url(self):
        return self.__base_url

    """This method should return next URL"""
    @abstractmethod
    def __solve(self):
        return NotImplementedError("Trying to call __solve in AbstractSolver.")