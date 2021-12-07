import tempfile
import inspect
import solution

example_input = inspect.cleandoc(
    """
    3,4,3,1,2
    """
)


def test_part_one():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        assert solution.part_one(f.name, 18) == 26
        assert solution.part_one(f.name, 80) == 5934


def test_advance_day():
    fish = solution.Fish(3)
    assert fish.timer == 3

    x, n = fish.advance_day()
    assert x == 2
    assert n == None

    x, n = fish.advance_day()
    assert x == 1
    assert n == None

    x, n = fish.advance_day()
    assert x == 0
    assert n == None

    x, n = fish.advance_day()
    assert x == 6
    assert n != None
    assert n.timer == 8


def test_part_two():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        assert solution.part_two(f.name, 256) == 26984457539
