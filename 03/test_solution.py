import inspect
import tempfile
import solution

example_input = inspect.cleandoc(
    """00100
       11110
       10110
       10111
       10101
       01111
       00111
       11100
       10000
       11001
       00010
       01010"""
)


def test_counts():
    assert solution.counts(["001", "000", "010"]) == [
        {0: 3, 1: 0},
        {0: 2, 1: 1},
        {0: 2, 1: 1},
    ]


def test_gamma():
    assert solution.gamma(solution.counts(["001", "000", "010"])) == 0
    assert solution.gamma(solution.counts(["001", "001", "010"])) == 1
    assert solution.gamma(solution.counts(["001", "010", "011"])) == 3


def test_epsilon():
    assert solution.epsilon(solution.counts(["001", "000", "010"])) == 7
    assert solution.epsilon(solution.counts(["001", "001", "010"])) == 6
    assert solution.epsilon(solution.counts(["001", "010", "011"])) == 4


def test_part_one():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        assert solution.gamma(solution.counts(str.split(example_input))) == 22
        assert solution.epsilon(solution.counts(str.split(example_input))) == 9
        assert solution.part_one(f.name) == 198


def test_part_two():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        numbers = str.split(example_input)
        assert solution.oxygen_generator_rating(numbers) == 23
        assert solution.co2_scrubber_rating(numbers) == 10
        assert solution.part_two(f.name) == 230
