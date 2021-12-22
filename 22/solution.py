import collections
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
            if match:
                value, *groups = match.groups()
                x_min, x_max, y_min, y_max, z_min, z_max = [int(s) for s in groups]
                step = Step(value, x_min, x_max, y_min, y_max, z_min, z_max)
                yield step


def run(steps):
    all_x_values = sorted(
        [
            v
            for step in steps
            for v in [step.x_min, step.x_min + 1, step.x_max, step.x_max + 1]
        ]
    )
    all_y_values = sorted(
        [
            v
            for step in steps
            for v in [step.y_min, step.y_min + 1, step.y_max, step.y_max + 1]
        ]
    )
    all_z_values = sorted(
        [
            v
            for step in steps
            for v in [step.z_min, step.z_min + 1, step.z_max, step.z_max + 1]
        ]
    )

    n = 4 * len(steps)
    # NOTE: too much memory w/ lists
    matrix = collections.defaultdict(
        lambda: collections.defaultdict(lambda: collections.defaultdict(lambda: False))
    )

    for step in steps:
        x_min_index = all_x_values.index(step.x_min)
        x_max_index = all_x_values.index(step.x_max + 1)
        y_min_index = all_y_values.index(step.y_min)
        y_max_index = all_y_values.index(step.y_max + 1)
        z_min_index = all_z_values.index(step.z_min)
        z_max_index = all_z_values.index(step.z_max + 1)

        for i in range(x_min_index, x_max_index):
            for j in range(y_min_index, y_max_index):
                for k in range(z_min_index, z_max_index):
                    if step.value == "on":
                        matrix[i][j][k] = True
                    else:
                        matrix[i][j][k] = False

    total_on = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[i][j][k]:
                    x_dimension = all_x_values[i + 1] - all_x_values[i]
                    y_dimension = all_y_values[j + 1] - all_y_values[j]
                    z_dimension = all_z_values[k + 1] - all_z_values[k]
                    this_prism = x_dimension * y_dimension * z_dimension
                    total_on += this_prism

    return total_on


def part_one(path):
    steps = list(read_input(path))
    limit = 50
    filtered_steps = [
        step
        for step in steps
        if step.x_min >= -limit
        and step.x_max <= limit
        and step.y_min >= -limit
        and step.y_max <= limit
        and step.z_min >= -limit
        and step.z_max <= limit
    ]
    return run(filtered_steps)


def part_two(path):
    steps = list(read_input(path))
    return run(steps)


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
