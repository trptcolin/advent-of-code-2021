import inspect
import tempfile
import solution

example_input = inspect.cleandoc(
    """6,10
       0,14
       9,10
       0,3
       10,4
       4,11
       6,0
       6,12
       4,1
       0,13
       10,12
       3,4
       3,0
       8,4
       1,10
       2,14
       8,10
       9,0

       fold along y=7
       fold along x=5"""
)


def test_part_one():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        assert solution.part_one(f.name) == 17


def test_read_input():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        instructions = solution.read_input(f.name)
        assert instructions.folds == [("y", 7), ("x", 5)]
        assert instructions.points == {
            (6, 10),
            (0, 14),
            (9, 10),
            (0, 3),
            (10, 4),
            (4, 11),
            (6, 0),
            (6, 12),
            (4, 1),
            (0, 13),
            (10, 12),
            (3, 4),
            (3, 0),
            (8, 4),
            (1, 10),
            (2, 14),
            (8, 10),
            (9, 0),
        }


def test_fold_once():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        instructions = solution.read_input(f.name)
        instructions.perform_fold()
        assert instructions.folds == [("x", 5)]
        assert instructions.points == {
            (0, 0),
            (2, 0),
            (3, 0),
            (6, 0),
            (9, 0),
            (0, 1),
            (4, 1),
            (6, 2),
            (10, 2),
            (0, 3),
            (4, 3),
            (1, 4),
            (3, 4),
            (6, 4),
            (8, 4),
            (9, 4),
            (10, 4),
        }


def test_fold_twice():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        instructions = solution.read_input(f.name)
        instructions.perform_fold()


def test_part_two():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        result = solution.part_two(f.name)
        assert result == inspect.cleandoc(
            """#####
               #...#
               #...#
               #...#
               #####"""
        )


def test_display():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        instructions = solution.read_input(f.name)
        lines = open("input_grid_1.txt").readlines()
        assert instructions.display() == "".join(lines).strip()
