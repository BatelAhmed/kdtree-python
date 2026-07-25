import random
import time

from kdtree import KDTree, distance_squared


def brute_force(points, target):
    return min(points, key=lambda p: distance_squared(p, target))
