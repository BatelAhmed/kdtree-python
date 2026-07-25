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
