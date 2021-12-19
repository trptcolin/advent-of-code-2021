import solution


def test_read_input():
    scanners = list(solution.read_input("example_input.txt"))
    assert len(scanners) == 5
    assert len(scanners[0].beacons) == 25
    assert len(scanners[1].beacons) == 25
    assert len(scanners[2].beacons) == 26
    assert len(scanners[3].beacons) == 25
    assert len(scanners[4].beacons) == 26


def test_overlap_1():
    scanners = list(solution.read_input("example_input.txt"))
    intersection = scanners[0].intersect(scanners[1])
    assert len(intersection) == 12
    assert scanners[1].translation == (68, -1246, -43)


def test_overlap_2():
    scanners = list(solution.read_input("example_input.txt"))
    scanners[0].intersect(scanners[1])
    intersection = scanners[1].intersect(scanners[4])
    assert len(intersection) == 12
    assert scanners[4].translation == (-20, -1133, 1061)


def test_overlap_3():
    scanners = list(solution.read_input("example_input.txt"))
    scanners[0].intersect(scanners[1])
    scanners[1].intersect(scanners[4])
    intersection = scanners[4].intersect(scanners[2])
    assert len(intersection) == 12
    assert scanners[2].translation == (1105, -1205, 1229)


def test_overlap_4():
    scanners = list(solution.read_input("example_input.txt"))
    scanners[0].intersect(scanners[1])
    scanners[1].intersect(scanners[4])
    scanners[4].intersect(scanners[2])
    intersection = scanners[1].intersect(scanners[3])
    assert len(intersection) == 12
    assert scanners[3].translation == (-92, -2380, -20)


def test_part_one():
    assert solution.part_one("example_input.txt") == 79


def test_part_one_and_two():
    assert solution.part_one_and_two("example_input.txt") == 3621
