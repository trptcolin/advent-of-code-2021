matching_end_brace = {"[": "]", "{": "}", "(": ")", "<": ">"}

end_braces = set(matching_end_brace.values())


class Error:

    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

    def __init__(self, expected, actual):
        self.expected = expected
        self.actual = actual

    def __eq__(self, other):
        if not isinstance(other, Error):
            return False
        return self.expected == other.expected and self.actual == other.actual

    def score(self):
        return self.scores[self.actual]


def find_error(line):
    chunk_stack = []
    for c in line:
        if len(chunk_stack) == 0:
            if c in end_braces:
                return Error("opening brace", c)
            else:
                chunk_stack.append(c)
        else:
            expected_end_brace = matching_end_brace[chunk_stack[-1]]
            if c == expected_end_brace:
                chunk_stack.pop()
            elif c in end_braces:
                return Error(expected_end_brace, c)
            else:
                chunk_stack.append(c)


def read_errors(path):
    with open(path) as f:
        for line in f:
            e = find_error(line.strip())
            if e != None:
                yield e


def part_one(path):
    return sum(e.score() for e in read_errors(path))


def part_two(path):
    pass


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
