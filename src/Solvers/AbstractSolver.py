__author__ = 'DimaTWL'

from abc import ABCMeta
from abc import abstractmethod


class AbstractSolver:
    __metaclass__ = ABCMeta

    def __init__(self, base_url):
        if isinstance(base_url, basestring):
            self.base_url = base_url
            self.next_url = None
        else:
            self.base_url = None
            self.next_url = None
            raise ValueError

    def __get_base_url(self):
        return self.base_url

    def get_next_url(self):
        self.solve()
        return self.next_url

    def __set_next_url(self, next_url):
        self.next_url = next_url

    @abstractmethod
    def solve(self):
        pass