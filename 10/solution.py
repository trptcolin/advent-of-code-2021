import statistics

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

    def __repr__(self):
        return f"Error(expected={self.expected}, actual={self.actual})"


class Complete:
    def __init__(self, line):
        self.line = line


class Incomplete:
    def __init__(self, line, chunk_stack):
        self.line = line
        self.chunk_stack = chunk_stack

    def __eq__(self, other):
        if not isinstance(other, Incomplete):
            return False
        return self.line == other.line and self.chunk_stack == other.chunk_stack

    def __repr__(self):
        return f"Incomplete(chunk_stack={self.chunk_stack})"

    def autocomplete(self):
        result = []
        while len(self.chunk_stack) > 0:
            c = self.chunk_stack.pop()
            result.append(matching_end_brace[c])
        return "".join(result)


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
    if len(chunk_stack) == 0:
        return Complete(line)
    else:
        return Incomplete(line, chunk_stack)


def read_errors(path):
    with open(path) as f:
        for line in f:
            yield find_error(line.strip())


completion_char_scores = {")": 1, "]": 2, "}": 3, ">": 4}


def completion_score(completion):
    score = 0
    for c in completion:
        score *= 5
        score += completion_char_scores[c]
    return score


def part_one(path):
    return sum(e.score() for e in read_errors(path) if isinstance(e, Error))


def part_two(path):
    incomplete_lines = (e for e in read_errors(path) if isinstance(e, Incomplete))
    scores = (completion_score(e.autocomplete()) for e in incomplete_lines)
    return statistics.median(scores)


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
