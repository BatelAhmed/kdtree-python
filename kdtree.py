from node import Node


def distance_squared(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def closer_point(target, p1, p2):
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    if distance_squared(target, p1) < distance_squared(target, p2):
        return p1
    return p2


class KDTree:
    def __init__(self, points=None):
        self.root = self._build(list(points), 0) if points else None

    def _build(self, points, depth):
        if not points:
            return None

        # splitting axis cycles with depth: x, y, x, y, ...
        axis = depth % 2
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

        axis = depth % 2
        if point[axis] < node.point[axis]:
            node.left = self._insert(node.left, point, depth + 1)
        else:
            node.right = self._insert(node.right, point, depth + 1)
        return node

    def nearest(self, target):
        return self._nearest(self.root, target, 0)

    def _nearest(self, node, target, depth):
        if node is None:
            return None

        axis = depth % 2

        # search the side the target is on first
        if target[axis] < node.point[axis]:
            near, far = node.left, node.right
        else:
            near, far = node.right, node.left

        best = closer_point(target, self._nearest(near, target, depth + 1), node.point)

        # the other side only matters if the splitting line is closer than the best so far
        if (target[axis] - node.point[axis]) ** 2 < distance_squared(target, best):
            best = closer_point(target, self._nearest(far, target, depth + 1), best)

        return best
