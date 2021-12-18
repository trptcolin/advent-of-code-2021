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
    # Directly from https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/ - thanks Bradfield folks!
    def shortest_path(self, start):
        all_locations = [(x, y) for x in range(self.x_size) for y in range(self.y_size)]
        distances = {location: float("infinity") for location in all_locations}
        previous = {location: [location] for location in all_locations}

        pq = [(0, start)]
        while len(pq) > 0:
            current_distance, current_vertex = heapq.heappop(pq)

            # don't traverse worse paths than we've seen
            if current_distance > distances[current_vertex]:
                continue

            neighbors = self.neighbors(current_vertex)
            for neighbor in neighbors:
                weight = self.risk_level(neighbor)
                distance = current_distance + weight

                # update distance to this neighbor if it's better
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
                    previous[neighbor] = current_vertex

        return previous, distances


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
