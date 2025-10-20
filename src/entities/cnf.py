from collections import defaultdict
from typing import Dict, List

from src.entities.variable_storage import VariableStorage


class ConjunctiveNormalForm:
    def __init__(self, title: str) -> None:
        self.title = title
        self.variables = VariableStorage()
        self.clauses = []
        self.values = set()
        self.lines = []

    def add(self, clauses: List[List[int]], comment: str = "") -> None:
        if comment:
            self.lines.append(f"c {comment}\n")

        for clause in clauses:
            self.clauses.append(clause)
            self.lines.append(f'{" ".join(str(literal) for literal in clause)} 0\n')

    def add_literals(self) -> None:
        self.add([[v] for v in self.variables.get_known()], "literals")

    def set_value(self, variable: int, value: bool) -> None:
        self.variables.set_value(index=variable, value=value)

    def save(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"p cnf {len(self.variables)} {len(self.clauses)}\n")
            f.writelines(self.lines)

    def statistic(self):
        clause_lengths = [len(clause) for clause in self.clauses]
        counts: Dict[int, int] = defaultdict(int)

        for clause in self.clauses:
            counts[len(clause)] += 1

        print(self.title)
        print(f"variables: {len(self.variables)} (real: {self.variables.real_count()}, fresh: {self.variables.fresh_count()})")
        print(f"clauses: {len(self.clauses)}, lengths (min / max / avg): {min(clause_lengths)} / {max(clause_lengths)} / {sum(clause_lengths) / len(self.clauses)}")

        for clause_length in sorted(counts.keys()):
            print(f"- {clause_length}-literal: {counts[clause_length]} ({counts[clause_length] / len(self.clauses):.2%})")
