import inspect
import tempfile
import solution

example_input = inspect.cleandoc(
    """1163751742
       1381373672
       2136511328
       3694931569
       7463417111
       1319128137
       1359912421
       3125421639
       1293138521
       2311944581"""
)


def read_input():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        return solution.read_input(f.name)


def test_read_input():
    cave_map = read_input()
    assert len(cave_map.grid) == 10
    assert len(cave_map.grid[0]) == 10
    assert cave_map.grid[0] == [1, 1, 6, 3, 7, 5, 1, 7, 4, 2]
    assert cave_map.grid[-1] == [2, 3, 1, 1, 9, 4, 4, 5, 8, 1]


def test_neighbors():
    cave_map = read_input()
    assert cave_map.neighbors((0, 0)) == [(0, 1), (1, 0)]
    assert cave_map.neighbors((1, 1)) == [(1, 0), (1, 2), (0, 1), (2, 1)]


def test_shortest_path():
    cave_map = read_input()
    previous, shortest = cave_map.shortest_path((0, 0))
    assert shortest[(9, 9)] == 40
    path = solution.render_path(previous, (0, 0), (9, 9))
    assert len(path) == 19


def test_part_one():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        assert solution.part_one(f.name) == 40


def test_part_two():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        assert solution.part_two(f.name) == 315


def test_increase_grid_size():
    cave_map = read_input()
    bigger_grid = solution.increase_grid_size(cave_map.grid)
    assert len(bigger_grid) == 50
    assert len(bigger_grid[0]) == 50
    assert (
        "".join([str(x) for x in bigger_grid[0]])
        == "11637517422274862853338597396444961841755517295286"
    )
    assert (
        "".join([str(x) for x in bigger_grid[-1]])
        == "67554889357866599146897761125791887223681299833479"
    )
