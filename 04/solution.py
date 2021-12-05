class Board:
    def __init__(self, lines):
        self.lines = lines
        self.values = set()
        for line in lines:
            for value in line:
                self.values.add(value)

    def mark(self, n):
        if n not in self.values:
            return
        for line in self.lines:
            for i, value in enumerate(line):
                if value == n:
                    line[i] = (value, "x")

    def has_horizontal_win(self):
        for i, line in enumerate(self.lines):
            win = all([type(value) == tuple for value in line])
            if win:
                return True

    def has_vertical_win(self):
        for i in range(len(self.lines[0])):
            win = all([type(line[i]) == tuple for line in self.lines])
            if win:
                return True

    def has_win(self):
        return self.has_horizontal_win() or self.has_vertical_win()

    def unmarked_numbers(self):
        results = []
        for line in self.lines:
            results.extend([value for value in line if type(value) != tuple])
        return results

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.lines == self.lines
        return False

    def score(self, n):
        return sum(self.unmarked_numbers()) * n


def read_board(f):
    lines = []
    blank_line = next(f, None)
    if blank_line == None:
        return None

    for _ in range(5):
        lines.append([int(x) for x in next(f).split()])
    return Board(lines)


def read_input(path):
    numbers = []
    boards = []
    with open(path) as f:
        numbers = [int(x) for x in next(f).split(",")]
        complete = False
        while not complete:
            board = read_board(f)
            if board == None:
                return numbers, boards
            else:
                boards.append(board)
    return numbers, boards


def part_one(path):
    numbers, boards = read_input(path)
    for n in numbers:
        for board in boards:
            board.mark(n)
            if board.has_win():
                return board.score(n)


def part_two(path):
    numbers, boards = read_input(path)
    board_indexes_to_play = set(range(len(boards)))

    for n in numbers:
        for i, board in enumerate(boards):
            if i not in board_indexes_to_play:
                continue
            board.mark(n)
            if board.has_win():
                if len(board_indexes_to_play) == 1:
                    board_index = board_indexes_to_play.pop()
                    return boards[board_index].score(n)
                board_indexes_to_play.remove(i)


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
