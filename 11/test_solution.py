import inspect
import tempfile
import solution
from solution import Grid, Octopus

small_example_input = inspect.cleandoc(
    """34543
       40004
       50005
       40004
       34543"""
)

large_example_input = inspect.cleandoc(
    """5483143223
       2745854711
       5264556173
       6141336146
       6357385478
       4167524645
       2176841721
       6882881134
       4846848554
       5283751526"""
)


def test_part_one():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(large_example_input, "UTF-8"))
        f.seek(0)

        assert solution.part_one(f.name) == 1656


def test_read_input():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(small_example_input, "UTF-8"))
        f.seek(0)

        grid = solution.read_input(f.name)
        assert grid == Grid(
            [
                [3, 4, 5, 4, 3],
                [4, 0, 0, 0, 4],
                [5, 0, 0, 0, 5],
                [4, 0, 0, 0, 4],
                [3, 4, 5, 4, 3],
            ]
        )


def test_neighbors():
    grid = Grid(
        [
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1],
        ]
    )
    assert grid.neighbors(Octopus(1, 0, 0)) == {
        Octopus(1, 1, 0),
        Octopus(1, 0, 1),
        Octopus(9, 1, 1),
    }
    assert grid.neighbors(Octopus(9, 1, 1)) == {
        Octopus(1, 0, 0),
        Octopus(1, 1, 0),
        Octopus(1, 2, 0),
        Octopus(1, 0, 1),
        Octopus(9, 2, 1),
        Octopus(1, 0, 2),
        Octopus(9, 1, 2),
        Octopus(1, 2, 2),
    }


def test_step():
    grid = Grid(
        [
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1],
        ]
    )
    grid.step()

    assert grid == Grid(
        [
            [3, 4, 5, 4, 3],
            [4, 0, 0, 0, 4],
            [5, 0, 0, 0, 5],
            [4, 0, 0, 0, 4],
            [3, 4, 5, 4, 3],
        ]
    )

    grid.step()

    assert grid == Grid(
        [
            [4, 5, 6, 5, 4],
            [5, 1, 1, 1, 5],
            [6, 1, 1, 1, 6],
            [5, 1, 1, 1, 5],
            [4, 5, 6, 5, 4],
        ]
    )


def test_larger_example_step():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(large_example_input, "UTF-8"))
        f.seek(0)

        grid = solution.read_input(f.name)
        grid.step()
        assert grid == Grid.from_string(
            inspect.cleandoc(
                """6594254334
                   3856965822
                   6375667284
                   7252447257
                   7468496589
                   5278635756
                   3287952832
                   7993992245
                   5957959665
                   6394862637
        """
            )
        )
        grid.step()
        assert grid == Grid.from_string(
            inspect.cleandoc(
                """8807476555
                   5089087054
                   8597889608
                   8485769600
                   8700908800
                   6600088989
                   6800005943
                   0000007456
                   9000000876
                   8700006848"""
            )
        )
