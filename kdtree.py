from node import Node


def distance_squared(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))


def closer_point(target, p1, p2):
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    if distance_squared(target, p1) < distance_squared(target, p2):
        return p1
    return p2


class KDTree:
    def __init__(self, points=None, k=2):
        self.k = k
        self.root = self._build(list(points), 0) if points else None

    def _build(self, points, depth):
        if not points:
            return None

        # splitting axis cycles with depth: x, y, x, y, ...
        axis = depth % self.k
        points.sort(key=lambda p: p[axis])
        mid = len(points) // 2

        # median as the root of each subtree keeps the tree balanced
        node = Node(points[mid])
        node.left = self._build(points[:mid], depth + 1)
        node.right = self._build(points[mid + 1:], depth + 1)
        return node

    def insert(self, point):
        self.root = self._insert(self.root, point, 0)

    def _insert(self, node, point, depth):
        if node is None:
            return Node(point)

        axis = depth % self.k
        if point[axis] < node.point[axis]:
            node.left = self._insert(node.left, point, depth + 1)
        else:
            node.right = self._insert(node.right, point, depth + 1)
        return node
