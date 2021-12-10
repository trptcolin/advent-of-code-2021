import inspect
import tempfile
import solution

example_input = inspect.cleandoc(
    """2199943210
       3987894921
       9856789892
       8767896789
       9899965678"""
)


def test_read_input():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        assert solution.read_input(f.name) == [
            [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
            [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
        ]


def test_part_one():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        assert solution.part_one(f.name) == 15


def test_basin_sizes():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        heightmap = solution.read_input(f.name)
        location_map = solution.LocationMap(heightmap)
        basins = solution.basin_sizes(location_map)
        assert sorted([len(basin) for basin in basins]) == [3, 9, 9, 14]


def test_part_two():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        assert solution.part_two(f.name) == 1134
