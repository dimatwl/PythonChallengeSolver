__author__ = 'DimaTWL'

from src.Solvers.AbstractSolver import AbstractSolver

class SolverFor1(AbstractSolver):

    def __init__(self, base_url):
        super(SolverFor1, self).__init__(base_url)

    def solve(self):
        return self.get_url_fetcher().fetch_url()