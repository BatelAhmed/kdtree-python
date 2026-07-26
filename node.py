class Node:
    # nodes only ever hold these three, saves memory on big trees
    __slots__ = ("point", "left", "right")

    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None
