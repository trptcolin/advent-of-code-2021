import itertools


def read_ints(path):
    with open(path) as f:
        for line in f:
            try:
                yield int(line)
            except:
                pass


# available directly in itertools in python 3.10+
def pairwise(xs):
    a, b = itertools.tee(xs)
    next(b, None)
    return zip(a, b)


def count_increases(values):
    pairs = pairwise(values)
    return len([(x, y) for (x, y) in pairs if x < y])


def part_one(path):
    values = read_ints(path)
    return count_increases(values)


def triplewise(xs):
    a, b, c = itertools.tee(xs, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return zip(a, b, c)


def triple_sums(xs):
    triples = triplewise(xs)
    return (a + b + c for (a, b, c) in triples)


def part_two(path):
    values = read_ints(path)
    sums = triple_sums(values)
    return count_increases(sums)


if __name__ == "__main__":
    print("Part 1:", part_one("./input.txt"))
    print("Part 2:", part_two("./input.txt"))
