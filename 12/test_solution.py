import inspect
import tempfile
import solution
from solution import Path

example_1_input = inspect.cleandoc(
    """start-A
       start-b
       A-c
       A-b
       b-d
       A-end
       b-end"""
)

example_2_input = inspect.cleandoc(
    """dc-end
       HN-start
       start-kj
       dc-start
       dc-HN
       LN-dc
       HN-end
       kj-sa
       kj-HN
       kj-dc"""
)

example_3_input = inspect.cleandoc(
    """fs-end
       he-DX
       fs-he
       start-DX
       pj-DX
       end-zg
       zg-sl
       zg-pj
       pj-he
       RW-he
       fs-DX
       pj-RW
       zg-RW
       start-pj
       he-WI
       zg-he
       pj-fs
       start-RW"""
)


def test_part_one():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_1_input, "UTF-8"))
        f.seek(0)

        assert solution.part_one(f.name) == 10


def test_valid_path():
    path = Path(0, ["start", "HN", "kj", "HN", "dc", "HN", "end"])
    assert path.is_valid() == True

    path = Path(0, ["start", "A", "c", "A", "c", "A", "end"])
    assert path.is_valid() == False

    path = Path(1, ["start", "A", "c", "A", "c", "A", "end"])
    assert path.is_valid() == True

    path = Path(1, ["start", "b", "A", "b", "A", "b", "end"])
    assert path.is_valid() == False


def test_part_one_bigger_example():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_2_input, "UTF-8"))
        f.seek(0)

        assert solution.part_one(f.name) == 19


def test_part_two():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_1_input, "UTF-8"))
        f.seek(0)

        assert solution.part_two(f.name) == 36


def test_part_two_bigger():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_2_input, "UTF-8"))
        f.seek(0)

        assert solution.part_two(f.name) == 103


def test_part_two_biggest():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_3_input, "UTF-8"))
        f.seek(0)

        assert solution.part_two(f.name) == 3509
