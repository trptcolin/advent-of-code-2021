class Octopus:
    def __init__(self, energy, x, y):
        self.energy = energy
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Octopus):
            return False
        return self.energy == other.energy and self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"{self.energy}"

    def __hash__(self):
        # hashing by position, not value: approximates object identity
        return hash((self.x, self.y))


class Grid:
    def from_string(s):
        return Grid([[int(x) for x in line.strip()] for line in s.split()])

    def __init__(self, values):
        self.grid_size = len(values)
        self.flashes = 0
        self.all_flashed_this_step = False
        self.octopi = [
            [Octopus(x, i, j) for i, x in enumerate(line)]
            for j, line in enumerate(values)
        ]

    def __repr__(self):
        return f"Grid({self.octopi})"

    def __eq__(self, other):
        if not isinstance(other, Grid):
            return False

        return self.octopi == other.octopi

    def neighbors(self, octopus):
        x = octopus.x
        y = octopus.y
        possible_neighbor_coordinates = [
            (x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1),
        ]
        actual_neighbor_coordinates = [
            (x, y)
            for (x, y) in possible_neighbor_coordinates
            if x > -1 and x < self.grid_size and y > -1 and y < self.grid_size
        ]
        return set([self.octopi[y][x] for x, y in actual_neighbor_coordinates])

    def step(self):
        all_flashed_this_step = set()
        to_process = set()

        for line in self.octopi:
            for octopus in line:
                octopus.energy += 1
                if octopus.energy > 9:
                    self.flashes += 1
                    all_flashed_this_step.add(octopus)
                    to_process.add(octopus)

        while len(to_process) > 0:
            octopus = to_process.pop()
            neighbors = self.neighbors(octopus)
            for neighbor in neighbors:
                neighbor.energy += 1
                if neighbor.energy > 9:
                    if neighbor not in all_flashed_this_step:
                        all_flashed_this_step.add(neighbor)
                        self.flashes += 1
                        to_process.add(neighbor)

        if len(all_flashed_this_step) == self.grid_size * self.grid_size:
            self.all_flashed_this_step = True
        else:
            self.all_flashed_this_step = False
        for octopus in all_flashed_this_step:
            octopus.energy = 0


def read_input(path):
    with open(path) as f:
        return Grid([[int(x) for x in line.strip()] for line in f])


def part_one(path):
    grid = read_input(path)
    for _ in range(100):
        grid.step()
    return grid.flashes


def part_two(path):
    grid = read_input(path)

    # arbitrarily capping it
    for i in range(10000):
        grid.step()
        if grid.all_flashed_this_step:
            return i + 1


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
