import re

point_regex = re.compile(r"(\d+),(\d+)")
fold_regex = re.compile(r"fold along (\w)=(\d+)")


class Instructions:
    def __init__(self, folds, points):
        self.folds = folds
        self.points = points

    def perform_fold(self):
        direction, value = self.folds.pop(0)
        if direction == "x":
            self.fold_vertical(value)
        else:
            self.fold_horizontal(value)

    def fold_vertical(self, n):
        updated_points = set()
        for x, y in self.points:
            updated_y = y
            if x < n:
                updated_x = x
            else:
                distance_away = x - n
                updated_x = x - (2 * distance_away)
            updated_points.add((updated_x, updated_y))
        self.points = updated_points

    def fold_horizontal(self, n):
        updated_points = set()
        for x, y in self.points:
            updated_x = x
            if y < n:
                updated_y = y
            else:
                distance_away = y - n
                updated_y = y - (2 * distance_away)
            updated_points.add((updated_x, updated_y))
        self.points = updated_points

    def display(self):
        max_x = 0
        max_y = 0
        for x, y in self.points:
            if x > max_x:
                max_x = x
            elif y > max_y:
                max_y = y

        grid = [["."] * (max_x + 1) for _ in range(max_y + 1)]
        for x, y in self.points:
            grid[y][x] = "#"
        return "\n".join(["".join(row) for row in grid])


def read_input(path):
    instructions = Instructions([], set())
    with open(path) as f:
        for line in f:
            point_match = re.match(point_regex, line)
            if point_match:
                x, y = point_match.groups()
                instructions.points.add((int(x), int(y)))
            else:
                fold_match = re.match(fold_regex, line)
                if fold_match:
                    direction, value = fold_match.groups()
                    instructions.folds.append((direction, int(value)))
    return instructions


def part_one(path):
    instructions = read_input(path)
    instructions.perform_fold()
    return len(instructions.points)


def part_two(path):
    instructions = read_input(path)
    for _ in range(len(instructions.folds)):
        print("folding")
        instructions.perform_fold()
    return instructions.display()


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
