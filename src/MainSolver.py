__author__ = 'DimaTWL'

from src.Solvers.SolverFor0 import SolverFor0
from src.Solvers.SolverFor1 import SolverFor1


class MainSolver:
    def __init__(self):
        self.__solvers = []
        self.__base_url = "http://www.pythonchallenge.com/pc/def/0.html"
        self.__next_url = self.__base_url
        self.__register_solvers()

    def __register_solvers(self):
        self.__solvers.append(SolverFor0)
        self.__solvers.append(SolverFor1)

    def solve_all(self):
        for solver_class in self.__solvers:
            solver = solver_class(self.__next_url)
            next_url = solver.get_next_url()
            if next_url is not None:
                self.__next_url = next_url
            else:
                raise ValueError("solver.get_next_url() is None.")
        print(self.__next_url)

