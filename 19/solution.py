import collections
import re

header_re = re.compile(r"--- scanner \d+.*")
beacon_re = re.compile(r"([\-\d]+),([\-\d]+),([\-\d]+)")

all_beacons = set()

orientations = [
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (x, -y, -z),
    lambda x, y, z: (x, z, -y),
    lambda x, y, z: (x, -z, y),
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (-x, z, y),
    lambda x, y, z: (-x, -z, -y),
    lambda x, y, z: (y, x, -z),
    lambda x, y, z: (y, -x, z),
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (y, -z, -x),
    lambda x, y, z: (-y, x, z),
    lambda x, y, z: (-y, -x, -z),
    lambda x, y, z: (-y, z, -x),
    lambda x, y, z: (-y, -z, x),
    lambda x, y, z: (z, x, y),
    lambda x, y, z: (z, -x, -y),
    lambda x, y, z: (z, y, -x),
    lambda x, y, z: (z, -y, x),
    lambda x, y, z: (-z, x, -y),
    lambda x, y, z: (-z, -x, y),
    lambda x, y, z: (-z, y, x),
    lambda x, y, z: (-z, -y, -x),
]


def subtract(x, y):
    a1, b1, c1 = x
    a2, b2, c2 = y
    return (a1 - a2, b1 - b2, c1 - c2)


def add(x, y):
    a1, b1, c1 = x
    a2, b2, c2 = y
    return (a1 + a2, b1 + b2, c1 + c2)


class Scanner:
    def __init__(self, beacons):
        self.beacons = beacons
        self.translation = (0, 0, 0)
        self.reference_scanner = None

    # IDEA: can we grow the known map instead of intersecting just with individual Scanners?
    def intersect(self, other):
        for orientation_index in range(24):
            rotate = orientations[orientation_index]
            other_reoriented = {rotate(*beacon) for beacon in other.beacons}
            # no need to search the whole list since we need 12 collisions
            for this_beacon in all_beacons:
                for other_beacon in other_reoriented:
                    difference = subtract(this_beacon, other_beacon)
                    moved = {add(beacon, difference) for beacon in other_reoriented}
                    matches = all_beacons.intersection(moved)
                    if len(matches) >= 12:
                        other.translation = difference
                        other.beacons = list(moved)
                        all_beacons.update(moved)
                        return matches


def read_input(path):
    with open(path) as f:
        beacons = []
        for line in f:
            if header_re.match(line):
                beacons = []
            elif line.isspace():
                yield Scanner(beacons)
            else:
                match = beacon_re.match(line)
                x, y, z = match.groups()
                beacons.append((int(x), int(y), int(z)))
        if len(beacons) > 0:
            yield Scanner(beacons)


def do_the_stuff(path):
    scanners = list(read_input(path))
    translated_scanners = [scanners[0]]
    all_beacons.update(set(scanners[0].beacons))
    untranslated_scanners = collections.deque(scanners[1:])
    while len(untranslated_scanners) > 0:
        scanner_to_translate = untranslated_scanners.popleft()
        print(
            "progress report... translating:",
            scanner_to_translate.beacons[0],
            "translated_scanners:",
            len(translated_scanners),
            "untranslated_scanners:",
            len(untranslated_scanners),
        )
        intersection = None
        for scanner in translated_scanners:
            intersection = scanner.intersect(scanner_to_translate)
            if intersection:
                translated_scanners.append(scanner_to_translate)
                break
        if not intersection:
            untranslated_scanners.append(scanner_to_translate)

    return translated_scanners


def part_one(path):
    translated_scanners = do_the_stuff(path)
    return len(all_beacons)


def manhattan_distance(x, y):
    a1, b1, c1 = x
    a2, b2, c2 = y
    return abs(a1 - a2) + abs(b1 - b2) + abs(c1 - c2)


def part_one_and_two(path):
    translated_scanners = do_the_stuff(path)
    print("Part 1:", len(all_beacons))

    biggest_distance_so_far = 0
    for a in translated_scanners:
        for b in translated_scanners:
            if a is not b:
                this_distance = manhattan_distance(a.translation, b.translation)
                if this_distance > biggest_distance_so_far:
                    biggest_distance_so_far = this_distance
    print("Part 2:", biggest_distance_so_far)
    return biggest_distance_so_far


if __name__ == "__main__":
    print(part_one_and_two("input.txt"))
