def read_input(path):
    with open(path) as f:
        return [[int(d) for d in line.strip()] for line in f]


def adjacent_to_point(i, j, i_limit, j_limit):
    indexes = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    return [
        (i, j)
        for (i, j) in indexes
        if i >= 0 and j >= 0 and i < i_limit and j < j_limit
    ]


def low_points(heightmap):
    results = []
    for i, line in enumerate(heightmap):
        for j, value in enumerate(line):
            if all(
                [
                    value < heightmap[i][j]
                    for (i, j) in adjacent_to_point(i, j, len(heightmap), len(line))
                ]
            ):
                results.append(value)
    return results


def part_one(path):
    heightmap = read_input(path)
    lows = low_points(heightmap)
    risk_levels = [x + 1 for x in lows]
    return sum(risk_levels)


def part_two(path):
    pass


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
