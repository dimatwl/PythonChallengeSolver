__author__ = 'DimaTWL'

from src.Solvers.AbstractSolver import AbstractSolver

class SolverFor0(AbstractSolver):

    def __init__(self, base_url):
        super(SolverFor0, self).__init__(base_url)

    """Actually there is nothing to solve here"""
    def solve(self):
        spitted_url_path = self.get_url_helper().get_url_path().split("/")
        splitted_last_part_in_path = spitted_url_path[-1].split(".")  # spitted_url_path[-1] means last element.
        splitted_last_part_in_path[0] = str(pow(2, 28))
        spitted_url_path[-1] = ".".join(splitted_last_part_in_path)
        new_url_path = "/".join(spitted_url_path)
        self.get_url_helper().set_url_path(new_url_path)
        return self.get_url_helper().get_url()