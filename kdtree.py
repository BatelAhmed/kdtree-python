def distance_squared(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))
