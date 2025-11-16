import re
import subprocess
from typing import Dict, List, Optional

from src.entities.variable_storage import VariableStorage
from src.utils.formulas import and_equality, at_least_k, at_most_k, between_k, lex_chain, lex_order, xor_chain


class ConjunctiveNormalForm:
    def __init__(self) -> None:
        self.variables = VariableStorage()
        self.variable2value = dict()
        self.model = dict()

        self.clauses = 0
        self.lines = []
        self.solution_lines = []
        self.ands = {}

    def add_var(self, name: str = "") -> int:
        return self.variables.get(name)

    def add_and_var(self, x: List[int]) -> int:
        t = self.add_var()
        self.add_clauses(clauses=and_equality(t, x))
        return t

    def add_at_least_k(self, x: List[int], k: int, comment: str = "") -> None:
        self.add_clauses(clauses=at_least_k(x=x, k=k, variables=self.variables), comment=comment)

    def add_at_most_k(self, x: List[int], k: int, comment: str = "") -> None:
        self.add_clauses(clauses=at_most_k(x=x, k=k, variables=self.variables), comment=comment)

    def add_between_k(self, x: List[int], k1: int, k2: int, comment: str = "") -> None:
        self.add_clauses(clauses=between_k(x=x, k1=k1, k2=k2, variables=self.variables), comment=comment)

    def add_lex_order(self, x: List[int], y: List[int], strict: bool, comment: str = "") -> None:
        self.add_clauses(clauses=lex_order(x, y, variables=self.variables, strict=strict), comment=comment)

    def add_lex_chain(self, x: List[List[int]], strict: bool, comment: str = "") -> None:
        self.add_clauses(clauses=lex_chain(x,  variables=self.variables, strict=strict), comment=comment)

    def add_xor(self, x: List[int], target: bool, comment: str = ""):
        clauses = xor_chain(x if target else [-x[0], *x[1:]], variables=self.variables)

        self.add_comment(comment)
        self.clauses += len(clauses)

        for clause in clauses:
            self.lines.append(f'x {" ".join(str(literal) for literal in clause)} 0\n')

    def add_clauses(self, clauses: List[List[int]], comment: str = "") -> None:
        self.add_comment(comment)
        self.clauses += len(clauses)

        for clause in clauses:
            self.lines.append(f'{" ".join(str(literal) for literal in clause)} 0\n')

    def add_comment(self, comment: str) -> None:
        if comment:
            self.lines.append(f"c {comment}\n")

    def set_value(self, x: int, value: bool) -> None:
        self.variable2value[x] = value

    def clear_values(self) -> None:
        self.variable2value.clear()

    def save(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"p cnf {len(self.variables)} {self.clauses + len(self.variable2value)}\n")
            f.writelines(self.lines)
            f.writelines(self.__encode_values())
            f.writelines(self.solution_lines)

    def solve(self, path: str, max_time: int = 0, threads: int = 2, seed: int = 0) -> Optional[bool]:
        self.save(path)
        self.model.clear()

        args = self.__get_solve_args(path=path, max_time=max_time, threads=threads, seed=seed)
        stdout = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
        return self.__parse_solution(stdout=stdout)

    def exclude_solution(self, variables: Dict[int, bool]) -> None:
        solution_line = " ".join(f"{-variable if value else variable}" for variable, value in variables.items())
        self.solution_lines.append(f"{solution_line} 0\n")

    def __getitem__(self, variable: int) -> bool:
        if not self.model:
            raise ValueError("Model is empty")

        return self.model[variable]

    def __encode_values(self) -> List[str]:
        return [f"{variable if value else -variable} 0\n" for variable, value in self.variable2value.items()]

    def __get_solve_args(self, path: str, max_time: int, threads: int, seed: int) -> List[str]:
        args = ["cryptominisat5", "--verb", "0"]

        if max_time > 0:
            args.extend(["--maxtime", f"{max_time}"])

        if seed > 0:
            args.extend(["-r", f"{seed + 1}"])

        args.extend(["--threads", f"{threads}"])
        args.append(path)
        return args

    def __parse_solution(self, stdout: str) -> Optional[bool]:
        text2sat = {"SATISFIABLE": True, "UNSATISFIABLE": False}

        lines = stdout.strip().split("\n")
        sat = [line[2:].strip() for line in lines if line.startswith("s ")]
        sat = None if not sat else text2sat.get(sat[0], None)

        if not sat:
            return sat

        real_variables = self.variables.get_real()
        solution = " ".join([line[2:].strip() for line in lines if line.startswith("v ")])
        literals = [int(literal) for literal in re.split(r" +", solution) if literal != "0"]
        literal2value = {abs(literal): literal > 0 for literal in literals if abs(literal) in real_variables}

        for variable in real_variables:
            self.model[variable] = literal2value[variable]

        solution_line = " ".join(f"{-variable if value else variable}" for variable, value in self.model.items())
        self.solution_lines.append(f"{solution_line} 0\n")
        return True
