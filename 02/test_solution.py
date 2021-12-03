import solution
import tempfile


def test_parse_input():
    with tempfile.NamedTemporaryFile() as f:
        f.write(b"up 1\ndown 2\nforward 3")
        f.seek(0)

        moves = solution.read_moves(f.name)
        assert list(moves) == [(0, -1), (0, 2), (3, 0)]


def test_parse_bad_input():
    with tempfile.NamedTemporaryFile() as f:
        f.write(b"unknown 50\nup 1\ndown 2\nforward 3")
        f.seek(0)

        moves = solution.read_moves(f.name)
        assert list(moves) == [(0, -1), (0, 2), (3, 0)]


def test_sum_distances():
    assert solution.sum_distances([]) == (0, 0)
    assert solution.sum_distances([(1, 0), (2, 0), (3, 0)]) == (6, 0)
    assert solution.sum_distances([(0, 1), (0, 2), (0, 3)]) == (0, 6)
    assert solution.sum_distances([(1, 1), (2, 2), (3, 3)]) == (6, 6)


def test_update_position():
    assert solution.update_position((0, 0, 0), (1, 0)) == (1, 0, 0)
    assert solution.update_position((0, 0, 0), (0, 1)) == (0, 0, 1)
    assert solution.update_position((1, 1, 1), (1, 0)) == (2, 2, 1)
    assert solution.update_position((1, 1, 1), (0, 1)) == (1, 1, 2)
    assert solution.update_position((1, 1, 2), (1, 0)) == (2, 3, 2)
    assert solution.update_position((1, 1, 2), (0, 1)) == (1, 1, 3)
    assert solution.update_position((1, 1, 2), (0, -1)) == (1, 1, 1)


def test_part_two():
    with tempfile.NamedTemporaryFile() as f:
        f.write(b"forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2")
        f.seek(0)

        assert solution.part_two(f.name) == 900
