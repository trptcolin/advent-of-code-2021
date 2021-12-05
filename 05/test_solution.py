import tempfile
import inspect
import solution

example_input = inspect.cleandoc(
    """0,9 -> 5,9
       8,0 -> 0,8
       9,4 -> 3,4
       2,2 -> 2,1
       7,0 -> 7,4
       6,4 -> 2,0
       0,9 -> 2,9
       3,4 -> 1,4
       0,0 -> 8,8
       5,5 -> 8,2"""
)


def test_part_one():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)
        assert solution.part_one(f.name) == 5


def test_part_two():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)
        assert solution.part_two(f.name) == 12


def test_make_line():
    # x ==
    assert solution.make_line((4, 0), (4, 3)) == [(4, 0), (4, 1), (4, 2), (4, 3)]
    assert solution.make_line((4, 0), (4, -2)) == [(4, 0), (4, -1), (4, -2)]

    # y ==
    assert solution.make_line((0, 9), (3, 9)) == [(0, 9), (1, 9), (2, 9), (3, 9)]
    assert solution.make_line((3, 9), (0, 9)) == [(3, 9), (2, 9), (1, 9), (0, 9)]


def test_make_line_including_diagonals():
    # x <, y <
    assert solution.make_line_including_diagonals((3, 0), (6, 3)) == [
        (3, 0),
        (4, 1),
        (5, 2),
        (6, 3),
    ]
    # x <, y >=
    assert solution.make_line_including_diagonals((1, 0), (3, -2)) == [
        (1, 0),
        (2, -1),
        (3, -2),
    ]
    # x >=, y <
    assert solution.make_line_including_diagonals((3, 0), (0, 3)) == [
        (3, 0),
        (2, 1),
        (1, 2),
        (0, 3),
    ]
    # x >=, y >=
    assert solution.make_line_including_diagonals((3, 1), (1, -1)) == [
        (3, 1),
        (2, 0),
        (1, -1),
    ]
