import math


def read_positions(path):
    with open(path) as f:
        line = next(f)
        return [int(x) for x in line.split(",")]


def cost_to_align(xs, x0):
    cost = 0
    for x in xs:
        cost += abs(x - x0)
    return cost


def part_one(path):
    # Idea: start searching at the bottom, and as soon as the cost increases
    # again, you're out of the local minimum (which is also a global minimum
    # since it's 1-dimensional). Binary search came to mind but you risk
    # leaping over the minimum and not being able to interpret changes.
    positions = read_positions(path)
    best_so_far = math.inf
    for n in range(0, max(positions) + 1):
        this_cost = cost_to_align(positions, n)
        if this_cost < best_so_far:
            best_so_far = this_cost
        else:
            return best_so_far


def part_two(path):
    pass


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
