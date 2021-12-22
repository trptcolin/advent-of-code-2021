from dataclasses import dataclass
import re

step_re = re.compile(
    r"(on|off) x=([\-\d]+)\.\.([\-\d]+),y=([\-\d]+)\.\.([\-\d]+),z=([\-\d]+)\.\.([\-\d]+)"
)


@dataclass
class Step:
    value: str
    x_min: int
    x_max: int
    y_min: int
    y_max: int
    z_min: int
    z_max: int


def read_input(path):
    with open(path) as f:
        for line in f:
            match = re.match(step_re, line)
            groups = match.groups()
            bounds = [int(s) for s in groups[1:]]
            step = Step(groups[0], *bounds)
            yield step


def part_one(path):
    steps = list(read_input(path))
    x_min = min([s.x_min for s in steps])
    y_min = min([s.y_min for s in steps])
    z_min = min([s.z_min for s in steps])
    x_max = max([s.x_max for s in steps])
    y_max = max([s.y_max for s in steps])
    z_max = max([s.z_max for s in steps])

    matrix = [
        [["off" for k in range(z_min, z_max + 1)] for j in range(y_min, y_max + 1)]
        for i in range(x_min, x_max + 1)
    ]
    print(x_min, x_max, y_min, y_max, z_min, z_max)
    for step in steps:
        print(step)
        for i in range(step.x_min - x_min, step.x_max - x_min + 1):
            for j in range(step.y_min - y_min, step.y_max - y_min + 1):
                for k in range(step.z_min - z_min, step.z_max - z_min + 1):
                    matrix[i][j][k] = step.value

    total_on = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix[0][0])):
                if matrix[i][j][k] == "on":
                    total_on += 1
    return total_on


def part_two(path):
    pass


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
