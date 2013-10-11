__author__ = 'DimaTWL'

from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import ParseResult


class UrlParser:
    def __init__(self, url, valid_url_scheme, valid_url_hostname):
        self.__parsed_url = None
        if isinstance(valid_url_scheme, str):
            self.__valid_url_scheme = valid_url_scheme
        else:
            raise ValueError("valid_url_scheme is not string. valid_url_scheme is '" + str(valid_url_scheme) + "'.")

        if isinstance(valid_url_hostname, str):
            self.__valid_url_hostname = valid_url_hostname
        else:
            raise ValueError("valid_url_hostname is not string. valid_url_hostname is '" + str(valid_url_hostname) + "'.")

        self.__check_url(url)

    def get_url_path(self):
        if self.__parsed_url is not None:
            return self.__parsed_url.path
        else:
            raise ValueError("self.__parsed_url is None")

    def set_url_path(self, new_url_path):
        if new_url_path is not None or isinstance(new_url_path, str):
            self.__parsed_url = ParseResult(
                scheme=self.__parsed_url.scheme,
                netloc=self.__parsed_url.netloc,
                path=new_url_path,
                params=self.__parsed_url.params,
                query=self.__parsed_url.query,
                fragment=self.__parsed_url.fragment)
        else:
            raise ValueError("new_url_path is not valid. new_url_path is " + str(new_url_path))

    def get_url(self):
        if self.__parsed_url is not None:
            return urlunparse(self.__parsed_url)
        else:
            raise ValueError("self.__parsed_url is None")

    def __check_url(self, url_to_check):
        if isinstance(url_to_check, str):
            self.__parsed_url = urlparse(url_to_check)
        else:
            raise ValueError("url_to_check is not string. url_to_check is '" + str(url_to_check) + "'.")
        if self.__parsed_url.scheme != self.__valid_url_scheme:
            raise ValueError(
                "base_url's scheme is not valid. Got '" +
                self.__parsed_url.scheme +
                "' but valid is '" +
                self.__valid_url_scheme +
                "'.")
        elif self.__parsed_url.hostname != self.__valid_url_hostname:
            raise ValueError(
                "base_url's path is not valid. Got '" +
                self.__parsed_url.hostname +
                "' but valid is '" +
                self.__valid_url_hostname +
                "'.")
        else:
            return True