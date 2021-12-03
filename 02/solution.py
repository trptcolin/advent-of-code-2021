import collections
import functools

direction_multipliers = collections.defaultdict(lambda _: (0, 0))
direction_multipliers.update({"forward": (1, 0), "up": (0, -1), "down": (0, 1)})


def read_moves(path):
    with open(path) as f:
        for line in f:
            direction, distance_str = line.split()
            try:
                distance = int(distance_str)
                x, y = direction_multipliers[direction]
                yield distance * x, distance * y
            except:
                pass


def add_tuple(t1, t2):
    a, b = t1
    x, y = t2
    return (a + x, b + y)


def sum_distances(moves):
    return functools.reduce(add_tuple, moves, (0, 0))


def part_one(path):
    moves = read_moves(path)
    x, y = sum_distances(moves)
    return x * y


def update_position(current, move):
    x, y, aim = current
    x1, y1 = move
    if x1 == 0:
        aim += y1
    else:
        x += x1
        y += aim * x1
    return x, y, aim


def part_two(path):
    moves = read_moves(path)
    x, y, aim = functools.reduce(update_position, moves, (0, 0, 0))
    return x * y


if __name__ == "__main__":
    print("Part 1:", part_one("input.txt"))
    print("Part 2:", part_two("input.txt"))
