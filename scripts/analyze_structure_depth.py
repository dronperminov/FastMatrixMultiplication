import time

from src.omega_optimization.structure_depth_optimizer import StructureDepthOptimizer


def main():
    n, m, p = 4, 4, 10
    structure = [(15, (1, 1, 2)), (85, (1, 1, 1))]

    eps = 1e-15
    max_depth = 200

    optimizer = StructureDepthOptimizer(n=n, m=m, p=p, structure=structure, eps=eps)
    optimizer.show()

    print("| depth |        omega        | omega / omega_prev | elapsed time |")
    prev_omega = optimizer.omega

    for depth in range(1, max_depth):
        t1 = time.time()
        omega = optimizer.optimize(depth=depth, x0=prev_omega * 0.99999)
        t2 = time.time()

        print(f"| {depth:5} | {omega:19.16f} | {omega / prev_omega:18.16f} | {t2 - t1:12.2f} |")
        prev_omega = omega



if __name__ == '__main__':
    main()
