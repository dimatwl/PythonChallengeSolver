__author__ = 'DimaTWL'

from abc import ABCMeta
from abc import abstractmethod

from urlparse import urlparse


class AbstractSolver:
    __metaclass__ = ABCMeta

    def __init__(self, base_url):
        self.__valid_url_scheme = "http"
        self.__valid_url_hostname = "www.pythonchallenge.com"
        self.__parsed_base_url = None
        if isinstance(base_url, basestring) and self.__check_url(base_url):
            self.__base_url = base_url
            self.__next_url = None
        else:
            self.__base_url = None
            self.__next_url = None
            self.__parsed_base_url = None
            raise ValueError("base_url is not a string.")

    def get_next_url(self):
        self.__next_url = self.solve()
        return self.__next_url

    def __get_base_url(self):
        return self.__base_url

    def __set_next_url(self, next_url):
        self.__next_url = next_url

    def __check_url(self, url_to_check):
        self.__parsed_base_url = urlparse(url_to_check)
        if self.__parsed_base_url.scheme != self.__valid_url_scheme:
            raise ValueError(
                "base_url's scheme is not valid. Got '" +
                self.__parsed_base_url.scheme +
                "' but valid is '" +
                self.__valid_url_scheme +
                "'.")
        elif self.__parsed_base_url.hostname != self.__valid_url_hostname:
            raise ValueError(
                "base_url's path is not valid. Got '" +
                self.__parsed_base_url.hostname +
                "' but valid is '" +
                self.__valid_url_hostname +
                "'.")
        else:
            return True


    @abstractmethod
    def solve(self):
        return "Stub"