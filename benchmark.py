import random
import time

from kdtree import KDTree, distance_squared


def brute_force(points, target):
    return min(points, key=lambda p: distance_squared(p, target))


if __name__ == "__main__":
    for n in (1000, 10000, 100000):
        points = [(random.uniform(0, 1000), random.uniform(0, 1000)) for _ in range(n)]
        targets = [(random.uniform(0, 1000), random.uniform(0, 1000)) for _ in range(100)]

        tree = KDTree(points)

        start = time.time()
        for t in targets:
            tree.nearest(t)
        tree_time = time.time() - start

        start = time.time()
        for t in targets:
            brute_force(points, t)
        brute_time = time.time() - start

        print(f"{n} points: kd-tree {tree_time:.4f}s, brute force {brute_time:.4f}s")
