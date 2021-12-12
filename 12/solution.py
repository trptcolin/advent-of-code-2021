import string
import collections

lowercase_letters = set(string.ascii_lowercase)


class Path:
    def __init__(self, small_cave_visit_limit, caves, counts=None):
        self.caves = caves
        self.small_cave_visit_limit = small_cave_visit_limit
        if counts == None:
            self.counts = collections.Counter(caves)
        else:
            self.counts = counts

    def with_added_cave(self, cave):
        counts = self.counts.copy()
        counts.update([cave])
        return Path(self.small_cave_visit_limit, [*self.caves, cave], counts)

    def is_valid(self):
        limit = self.small_cave_visit_limit
        small_cave_repeat_visits = 0
        for cave in self.counts:
            if cave[0] in lowercase_letters:
                if self.counts[cave] > 2:
                    return False
                if self.counts[cave] > 1:
                    small_cave_repeat_visits += 1
                    if small_cave_repeat_visits > self.small_cave_visit_limit:
                        return False

        return True

    def __repr__(self):
        return f"Path({self.small_cave_visit_limit},{self.caves})"


class CaveMap:
    def __init__(self):
        self.locations = {}
        self.small_cave_visit_limit = 0

    def add_path(self, start, end):
        if start in self.locations:
            existing_outs = self.locations[start]
            existing_outs.add(end)
        else:
            self.locations[start] = {end}

    def find_routes(self, this_cave=None, this_path=None, completed_routes=None):
        if this_cave == None:
            this_cave = "start"
        if this_path == None:
            this_path = Path(self.small_cave_visit_limit, [this_cave])
        if completed_routes == None:
            completed_routes = []
        end_cave = "end"

        if not this_path.is_valid():
            return

        if this_cave == end_cave:
            completed_routes.append(this_path)
            return

        neighbors = self.locations[this_cave]

        for neighbor in neighbors:
            if neighbor == "start":
                continue
            path = this_path.with_added_cave(neighbor)
            if path.is_valid():
                self.find_routes(neighbor, path, completed_routes)
        return completed_routes


def read_input(path):
    with open(path) as f:
        for line in f:
            yield line


def make_map(lines):
    cave_map = CaveMap()
    for line in lines:
        a, b = [name for name in line.strip().split("-")]
        cave_map.add_path(a, b)
        cave_map.add_path(b, a)
    return cave_map


def part_one(path):
    m = make_map(read_input(path))
    m.small_cave_visit_limit = 0
    routes = m.find_routes()
    return len(routes)


def part_two(path):
    m = make_map(read_input(path))
    m.small_cave_visit_limit = 1
    routes = m.find_routes()
    return len(routes)


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
