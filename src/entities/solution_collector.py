from typing import List

from ortools.sat.python.cp_model import CpSolverSolutionCallback, IntVar


class SolutionCollector(CpSolverSolutionCallback):
    def __init__(self, u: List[List[IntVar]], v: List[List[IntVar]], w: List[List[IntVar]], max_solutions: int):
        CpSolverSolutionCallback.__init__(self)
        self.u = u
        self.v = v
        self.w = w
        self.max_solutions = max_solutions
        self.solutions = []

    def on_solution_callback(self):
        u = [[self.Value(value) for value in row] for row in self.u]
        v = [[self.Value(value) for value in row] for row in self.v]
        w = [[self.Value(value) for value in row] for row in self.w]
        self.solutions.append((u, v, w))

        if len(self.solutions) >= self.max_solutions:
            self.stop_search()
