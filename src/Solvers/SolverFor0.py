__author__ = 'DimaTWL'

from src.Solvers.AbstractSolver import AbstractSolver

class SolverFor0(AbstractSolver):

    def __init__(self, base_url):
        super(SolverFor0, self).__init__(base_url)

    """Actually there is nothing to solve here"""
    def solve(self):
        split_url_path = self.get_url_parser().get_url_path().split("/")
        split_last_part_in_path = split_url_path[-1].split(".")  # split_url_path[-1] means last element.
        split_last_part_in_path[0] = str(pow(2, 28))
        split_url_path[-1] = ".".join(split_last_part_in_path)
        new_url_path = "/".join(split_url_path)
        self.get_url_parser().set_url_path(new_url_path)
        return self.get_url_parser().get_url()