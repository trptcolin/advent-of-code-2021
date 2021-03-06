import re


class Target:
    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max


def read_input(path):
    input_regex = re.compile(r"target area: x=(.*)\.\.(.*), y=(.*)\.\.(.*)$")
    with open(path) as f:
        input_text = next(f).strip()
        groups = re.match(input_regex, input_text).groups()
        return Target(*[int(group) for group in groups])


class Probe:
    def __init__(self, x, y, x_velocity, y_velocity):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def step(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        if self.x_velocity < 0:
            self.x_velocity += 1
        elif self.x_velocity > 0:
            self.x_velocity -= 1
        self.y_velocity -= 1


def find_hits(target):
    overall_highest_y = -float("infinity")
    all_hits = set()

    max_possible_y = max(abs(target.y_min), abs(target.y_max))
    min_possible_y = min(-abs(target.y_min), -abs(target.y_max))

    for x_velocity in range(target.x_max + 1):
        for y_velocity in range(min_possible_y, max_possible_y + 1):
            probe = Probe(0, 0, x_velocity, y_velocity)
            this_highest_y = -float("infinity")
            while probe.x < target.x_max and probe.y > target.y_min:
                this_highest_y = max(probe.y, this_highest_y)
                probe.step()
                if (
                    target.x_min <= probe.x <= target.x_max
                    and target.y_min <= probe.y <= target.y_max
                ):
                    overall_highest_y = max(overall_highest_y, this_highest_y)
                    all_hits.add((x_velocity, y_velocity))

    return overall_highest_y, all_hits


def part_one(path):
    target = read_input(path)
    highest_y, all_hits = find_hits(target)
    return highest_y


def part_two(path):
    target = read_input(path)
    highest_y, all_hits = find_hits(target)
    return len(all_hits)


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
