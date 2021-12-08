import tempfile
import inspect
import solution

example_input = inspect.cleandoc(
    """
    16,1,2,0,4,2,7,1,2,14
    """
)


def test_read_positions():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        positions = solution.read_positions(f.name)
        assert positions == [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_cost_to_align():
    xs = [1, 2, 3]
    assert solution.cost_to_align(xs, 0) == 6
    assert solution.cost_to_align(xs, 1) == 3
    assert solution.cost_to_align(xs, 2) == 2
    assert solution.cost_to_align(xs, 3) == 3


def test_cost_to_align_from_example():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        positions = solution.read_positions(f.name)
        assert positions == [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        assert solution.cost_to_align(positions, 1) == 41
        assert solution.cost_to_align(positions, 2) == 37
        assert solution.cost_to_align(positions, 3) == 39
        assert solution.cost_to_align(positions, 10) == 71


def test_part_one():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        assert solution.part_one(f.name) == 37


def test_nonlinear_cost_to_align():
    xs = [1, 2, 3]
    assert solution.nonlinear_cost_to_align(xs, 0) == 1 + (1 + 2) + (1 + 2 + 3)


def test_nonlinear_cost_to_align_from_example():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        positions = solution.read_positions(f.name)
        assert positions == [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        assert solution.nonlinear_cost_to_align(positions, 1) == 242
        assert solution.nonlinear_cost_to_align(positions, 2) == 206
        assert solution.nonlinear_cost_to_align(positions, 3) == 183
        assert solution.nonlinear_cost_to_align(positions, 4) == 170
        assert solution.nonlinear_cost_to_align(positions, 5) == 168
        assert solution.nonlinear_cost_to_align(positions, 6) == 176
        assert solution.nonlinear_cost_to_align(positions, 7) == 194
        assert solution.nonlinear_cost_to_align(positions, 8) == 223


def test_part_two():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        assert solution.part_two(f.name) == 168
