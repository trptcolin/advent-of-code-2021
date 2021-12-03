import solution
import tempfile


def test_read_ints():
    with tempfile.NamedTemporaryFile() as f:
        f.write(b"1\n2\n3\n4\n5")
        f.seek(0)

        xs = solution.read_ints(f.name)
        assert list(xs) == [1, 2, 3, 4, 5]
    with tempfile.NamedTemporaryFile() as f:
        f.write(b"1\n2\nasdf\n4\n5")
        f.seek(0)

        xs = solution.read_ints(f.name)
        assert list(xs) == [1, 2, 4, 5]


def test_pairwise():
    assert list(solution.pairwise([])) == []
    assert list(solution.pairwise([1])) == []
    assert list(solution.pairwise([1, 2])) == [(1, 2)]
    assert list(solution.pairwise([1, 2, 3])) == [(1, 2), (2, 3)]
    assert list(solution.pairwise(range(5))) == [(0, 1), (1, 2), (2, 3), (3, 4)]


def test_triplewise():
    assert list(solution.triplewise([])) == []
    assert list(solution.triplewise([1])) == []
    assert list(solution.triplewise([1, 2])) == []
    assert list(solution.triplewise([1, 2, 3])) == [(1, 2, 3)]
    assert list(solution.triplewise(range(5))) == [(0, 1, 2), (1, 2, 3), (2, 3, 4)]


def test_count_increases():
    assert solution.count_increases([]) == 0
    assert solution.count_increases([0]) == 0
    assert solution.count_increases([1, 0]) == 0
    assert solution.count_increases([1, 1]) == 0
    assert solution.count_increases([0, 1]) == 1
    assert solution.count_increases([0, 1, 2]) == 2
    assert solution.count_increases([0, 2, 1, 2]) == 2
    assert solution.count_increases([0, 3, 1, 2]) == 2


def test_triple_sums():
    assert list(solution.triple_sums([])) == []
    assert list(solution.triple_sums([1])) == []
    assert list(solution.triple_sums([1, 2])) == []
    assert list(solution.triple_sums([1, 2, 3])) == [6]
    assert list(solution.triple_sums([1, 2, 3, 4])) == [6, 9]
