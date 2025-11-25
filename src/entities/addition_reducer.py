from src.entities.addition_minimization import AdditionMinimization
from src.schemes.scheme import Scheme


class AdditionReducer:
    def __init__(self, max_loops: int, max_size: int):
        self.max_loops = max_loops
        self.max_size = max_size

    def reduce(self, scheme: Scheme, mode: str) -> dict:
        u_expressions = [[scheme.u[index][i] for i in range(scheme.nn[0])] for index in range(scheme.m)]
        v_expressions = [[scheme.v[index][i] for i in range(scheme.nn[1])] for index in range(scheme.m)]
        w_expressions = [[scheme.w[index][i] for index in range(scheme.m)] for i in range(scheme.nn[2])]

        u_minimization = AdditionMinimization(u_expressions, real_variables=scheme.nn[0], max_size=self.max_size)
        v_minimization = AdditionMinimization(v_expressions, real_variables=scheme.nn[1], max_size=self.max_size)
        w_minimization = AdditionMinimization(w_expressions, real_variables=scheme.m, max_size=self.max_size)

        u_indices, u_fresh, u_additions = u_minimization.solve(mode=mode, loops=self.max_loops)
        v_indices, v_fresh, v_additions = v_minimization.solve(mode=mode, loops=self.max_loops)
        w_indices, w_fresh, w_additions = w_minimization.solve(mode=mode, loops=self.max_loops)

        return {
            "n": scheme.n,
            "m": scheme.m,
            "z2": scheme.z2,
            "complexity": {
                "naive": scheme.complexity(),
                "reduced": u_additions + v_additions + w_additions
            },
            "u_fresh": u_fresh,
            "v_fresh": v_fresh,
            "w_fresh": w_fresh,
            "u": u_indices,
            "v": v_indices,
            "w": w_indices
        }
