__author__ = 'DimaTWL'

from Solvers.SolverFor0 import SolverFor0

class MainSolver:
    def __init__(self):
        pass

    def solve_all(self):
        solver = SolverFor0("http://www.pythonchallenge.com/pc/def/0.html")
        solver.solve()
