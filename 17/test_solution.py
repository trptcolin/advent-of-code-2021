import tempfile
import solution

example_input = "target area: x=20..30, y=-10..-5\n"


def read_input():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        return solution.read_input(f.name)


def test_read_input():
    target = read_input()
    assert target.x_min == 20
    assert target.x_max == 30
    assert target.y_min == -10
    assert target.y_max == -5


def test_part_one():
    target = read_input()
    highest_y, all_hits = solution.find_hits(target)
    assert highest_y == 45
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)
        assert solution.part_one(f.name) == 45


def test_part_two():
    target = read_input()
    highest_y, all_hits = solution.find_hits(target)
    assert len(all_hits) == 112
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)
        assert solution.part_two(f.name) == 112
