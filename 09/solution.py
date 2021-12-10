import functools
import operator


def read_input(path):
    with open(path) as f:
        return [[int(d) for d in line.strip()] for line in f]


def neighbors(location, location_map):
    i = location.x
    j = location.y
    indexes = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    return [
        location_map.locations[i][j]
        for (i, j) in indexes
        if i >= 0 and j >= 0 and i < location_map.i_limit and j < location_map.j_limit
    ]


class Location:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height

    def __repr__(self):
        return f"Location(x:{self.x}, y:{self.y}, height:{self.height})"


class LocationMap:
    def __init__(self, heightmap):
        self.locations = []
        for i, line in enumerate(heightmap):
            if len(self.locations) <= i:
                self.locations.append([])
            for j, value in enumerate(line):
                self.locations[i].append(Location(i, j, value))
        self.i_limit = len(self.locations)
        self.j_limit = len(self.locations[0])


def is_lower_than_all_neighbors(location, location_map):
    x = location.x
    y = location.y
    return all(
        [
            location.height < neighbor.height
            for neighbor in neighbors(location, location_map)
        ]
    )


def low_points(location_map):
    results = []
    for i, line in enumerate(location_map.locations):
        for j, location in enumerate(line):
            if is_lower_than_all_neighbors(location, location_map):
                results.append(location)
    return results


def basin_sizes(location_map):
    lows = low_points(location_map)
    basins = []
    for i, low in enumerate(lows):
        basin = set()
        basin.add(low)
        process_queue = []
        process_queue.append(low)
        while len(process_queue) > 0:
            location = process_queue.pop()
            for neighbor in neighbors(location, location_map):
                if neighbor in basin:
                    continue
                if neighbor.height < 9 and neighbor.height >= location.height:
                    process_queue.append(neighbor)
                    basin.add(neighbor)
        basins.append(basin)
    return basins


def part_one(path):
    heightmap = read_input(path)
    location_map = LocationMap(heightmap)
    lows = low_points(location_map)
    risk_levels = [x.height + 1 for x in lows]
    return sum(risk_levels)


def part_two(path):
    heightmap = read_input(path)
    location_map = LocationMap(heightmap)
    basins = basin_sizes(location_map)
    biggest_3_basin_sizes = sorted([len(basin) for basin in basins], reverse=True)[:3]

    return functools.reduce(operator.mul, biggest_3_basin_sizes)


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
