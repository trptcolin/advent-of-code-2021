import tempfile
import inspect
import solution

example_input = inspect.cleandoc(
    """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

    22 13 17 11  0
     8  2 23  4 24
    21  9 14 16  7
     6 10  3 18  5
     1 12 20 15 19

     3 15  0  2 22
     9 18 13 17  5
    19  8  7 25 23
    20 11 10 24  4
    14 21 16 12  6

    14 21 17 24  4
    10 16 15  9 19
    18  8 23 26 20
    22 11 13  6  5
     2  0 12  3  7"""
)


def test_read_input():
    with tempfile.NamedTemporaryFile() as f:
        f.write(
            b"5,6,7\n"
            b"\n"
            b" 0  1  2  3  4\n"
            b" 5  6  7  8  9\n"
            b"10 11 12 13 14\n"
            b"15 16 17 18 19\n"
            b"20 21 22 23 24\n"
        )
        f.seek(0)

        moves, boards = solution.read_input(f.name)
        assert moves == [5, 6, 7]
        assert len(boards) == 1
        board = boards[0]
        assert board == solution.Board(
            [
                [0, 1, 2, 3, 4],
                [5, 6, 7, 8, 9],
                [10, 11, 12, 13, 14],
                [15, 16, 17, 18, 19],
                [20, 21, 22, 23, 24],
            ]
        )


def test_part_one():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        assert solution.part_one(f.name) == 4512


def test_part_two():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        assert solution.part_two(f.name) == 1924
