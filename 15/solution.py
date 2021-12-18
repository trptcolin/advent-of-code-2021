import sys
import heapq


class CaveMap:
    def __init__(self, grid):
        self.grid = grid
        self.x_size = len(grid[0])
        self.y_size = len(grid)

    def neighbors(self, location):
        x, y = location
        possible_neighbors = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
        return [
            (x, y)
            for x, y in possible_neighbors
            if x > -1 and y > -1 and x < self.x_size and y < self.y_size
        ]

    def risk_level(self, position):
        x, y = position
        return self.grid[y][x]

    # This is Dijkstra's algorithm we're just coding in it
    def shortest_path(self, start=None, end=None):
        if not start:
            start = (0, 0)
        if not end:
            end = (self.x_size - 1, self.y_size - 1)

        unvisited = [
            (self.risk_level((x, y)), (x, y))
            for x in range(self.x_size)
            for y in range(self.y_size)
        ]

        max_value = sys.maxsize
        shortest = {}
        for risk_level, location in unvisited:
            shortest[location] = max_value

        shortest[start] = 0
        previous = {}

        while len(unvisited) > 0:
            current_min = None
            for risk_level, location in unvisited:
                if current_min == None:
                    current_min = location
                elif shortest[location] < shortest[current_min]:
                    current_min = location

            neighbors = self.neighbors(current_min)

            for neighbor in neighbors:
                best_so_far = shortest[current_min] + self.risk_level(neighbor)
                if best_so_far < shortest[neighbor]:
                    shortest[neighbor] = best_so_far
                    previous[neighbor] = current_min

            unvisited.remove((self.risk_level(current_min), current_min))

        return previous, shortest


def render_path(previous, start, end):
    path = []
    location = end
    while location != start:
        path.append(location)
        location = previous[location]
    path.append(start)
    path.reverse()
    return path


def read_input(path):
    with open(path) as f:
        grid = [[int(c) for c in line.strip()] for line in f]
        return CaveMap(grid)


def add_risk(value, n):
    proposed_risk = value + n
    if proposed_risk > 9:
        return proposed_risk - 9
    else:
        return proposed_risk


def increase_grid_size(grid):
    x_len = len(grid[0])
    y_len = len(grid)
    bigger_grid = [[None for i in range(x_len * 5)] for j in range(y_len * 5)]
    for x in range(5):
        for y in range(5):
            for j, line in enumerate(grid):
                for i, value in enumerate(line):
                    risk = add_risk(value, x + y)
                    bigger_grid[y * y_len + j][x * x_len + i] = risk
    return bigger_grid


def part_one(path):
    cave_map = read_input(path)
    previous, shortest = cave_map.shortest_path((0, 0))
    return shortest[(cave_map.x_size - 1, cave_map.y_size - 1)]


def part_two(path):
    small_map = read_input(path)
    cave_map = CaveMap(increase_grid_size(small_map.grid))
    previous, shortest = cave_map.shortest_path((0, 0))
    return shortest[(cave_map.x_size - 1, cave_map.y_size - 1)]


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
