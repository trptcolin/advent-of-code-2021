import collections
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


def read_example(p=solution.Polymer):
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        return solution.read_input(f.name, p)


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


def test_advance_better():
    polymer = read_example(solution.BetterPolymer)
    assert polymer.element_counts() == collections.Counter("NNCB")
    polymer.advance()
    assert polymer.element_counts() == collections.Counter("NCNBCHB")
    polymer.advance()
    assert polymer.element_counts() == collections.Counter("NBCCNBBBCBHCB")
    polymer.advance()
    assert polymer.element_counts() == collections.Counter("NBBBCNCCNBBNBNBBCHBHHBCHB")
    polymer.advance()
    assert polymer.element_counts() == collections.Counter(
        "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
    )


def test_part_two():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        assert solution.part_two(f.name) == 2188189693529
