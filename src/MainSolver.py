__author__ = 'DimaTWL'

from Solvers.SolverFor0 import SolverFor0

class MainSolver:
    def __init__(self):
        self.solvers = []
        self.base_url = "http://www.pythonchallenge.com/pc/def/0.html"
        self.next_url = self.base_url
        self.__register_solvers()

    def __register_solvers(self):
        self.solvers.append(SolverFor0)

    def solve_all(self):
        for solver_class in self.solvers:
            solver = solver_class(self.next_url)
            solver.solve()
            if solver.get_next_url() is not None:
                self.next_url = solver.get_next_url()
            else:
                raise ValueError

