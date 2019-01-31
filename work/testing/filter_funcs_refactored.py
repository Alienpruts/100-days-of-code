def is_positive(n):
    return n > 0


def filter_ints(v):
    v = [num for num in v if num!= 0]
    return [num for num in v if is_positive(num)]
