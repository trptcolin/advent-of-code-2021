import inspect
import tempfile
import solution

example_input = inspect.cleandoc(
    """NNCB

       CH -> B
       HH -> N
       CB -> H
       NH -> C
       HB -> C
       HC -> B
       HN -> C
       NN -> C
       BH -> H
       NC -> B
       NB -> B
       BN -> B
       BB -> N
       BC -> B
       CC -> N
       CN -> C"""
)


def read_example():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        return solution.read_input(f.name)


def test_read_input():
    polymer = read_example()
    assert polymer.template == "NNCB"
    assert len(polymer.rules) == 16
    assert polymer.rules["CH"] == "B"
    assert polymer.rules["CN"] == "C"


def test_advance():
    polymer = read_example()
    polymer.advance()
    assert polymer.template == "NCNBCHB"
    polymer.advance()
    assert polymer.template == "NBCCNBBBCBHCB"
    polymer.advance()
    assert polymer.template == "NBBBCNCCNBBNBNBBCHBHHBCHB"
    polymer.advance()
    assert polymer.template == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"


def test_many_advances():
    polymer = read_example()
    for _ in range(10):
        polymer.advance()
    assert len(polymer.template) == 3073


def test_part_one():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        assert solution.part_one(f.name) == 1588
