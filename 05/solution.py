def make_line(x, y):
    a, b = x
    c, d = y
    if a == c:
        if b < d:
            return [(a, i) for i in range(b, d + 1)]
        else:
            return [(a, i) for i in range(b, d - 1, -1)]
    elif b == d:
        if a < c:
            return [(i, b) for i in range(a, c + 1)]
        else:
            return [(i, b) for i in range(a, c - 1, -1)]
    else:
        return []


def make_line_including_diagonals(x, y):
    a, b = x
    c, d = y

    results = make_line(x, y)
    if results != []:
        return results

    if a < c and b < d:
        for i in range(a, c + 1):
            results.append((i, b + (i - a)))
    elif a < c and b >= d:
        for i in range(a, c + 1):
            results.append((i, b - (i - a)))
    elif a >= c and b < d:
        for i in range(a, c - 1, -1):
            results.append((i, b - (i - a)))
    else:  # a >= c and b >= d:
        for i in range(a, c - 1, -1):
            results.append((i, b + (i - a)))

    return results


def read_input(path, line_maker):
    result = []
    with open(path) as f:
        for line in f:
            a, b = line.split(" -> ")
            a = [int(x) for x in a.split(",")]
            b = [int(x) for x in b.split(",")]
            result.append(line_maker(a, b))
        return result


def count_overlaps(lines):
    board = {}
    for line in lines:
        for point in line:
            if point in board:
                board[point] += 1
            else:
                board[point] = 1
    overlaps = 0
    for k in board:
        if board[k] > 1:
            overlaps += 1
    return overlaps


def part_one(path):
    lines = read_input(path, make_line)
    return count_overlaps(lines)


def part_two(path):
    lines = read_input(path, make_line_including_diagonals)
    return count_overlaps(lines)


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
