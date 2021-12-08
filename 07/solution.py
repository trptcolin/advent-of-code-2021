import math


def read_positions(path):
    with open(path) as f:
        line = next(f)
        return [int(x) for x in line.split(",")]


def distance(x, y):
    return abs(x - y)


def cost_to_align(xs, x0):
    cost = 0
    for x in xs:
        cost += distance(x, x0)
    return cost


def sum_1_to_n(n):
    return int(n * (n + 1) / 2)


def nonlinear_cost_to_align(xs, x0):
    return sum([sum_1_to_n(distance(x, x0)) for x in xs])


def find_best_cost(positions, cost_function):
    # Idea: start searching at the bottom, and as soon as the cost increases
    # again, you're out of the local minimum (which is also a global minimum
    # since it's 1-dimensional - feels more obvious for linear than nonlinear
    # cost functions...). Binary search came to mind but you risk leaping over
    # the minimum and not being able to interpret changes.
    best_so_far = math.inf
    for n in range(0, max(positions) + 1):
        this_cost = cost_function(positions, n)
        if this_cost < best_so_far:
            best_so_far = this_cost
        else:
            return best_so_far


def part_one(path):
    positions = read_positions(path)
    return find_best_cost(positions, cost_to_align)


def part_two(path):
    positions = read_positions(path)
    return find_best_cost(positions, nonlinear_cost_to_align)


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
