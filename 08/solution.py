import collections


class Signal:
    def parse(text):
        patterns, outputs = text.strip().split(" | ")
        patterns = [set(s) for s in patterns.split(" ")]
        outputs = [set(s) for s in outputs.split(" ")]
        return Signal(patterns, outputs)

    def __init__(self, signal_patterns, outputs):
        self.signal_patterns = signal_patterns
        self.outputs = outputs
        self.mappings = {}

    def find_unique_patterns(self):
        patterns_to_remove = []
        for pattern in self.signal_patterns:
            if len(pattern) == 2:
                self.mappings[1] = pattern
                patterns_to_remove.append(pattern)
            elif len(pattern) == 4:
                self.mappings[4] = pattern
                patterns_to_remove.append(pattern)
            elif len(pattern) == 3:
                self.mappings[7] = pattern
                patterns_to_remove.append(pattern)
            elif len(pattern) == 7:
                self.mappings[8] = pattern
                patterns_to_remove.append(pattern)
        for pattern in patterns_to_remove:
            self.signal_patterns.remove(pattern)

    def find_six(self):
        patterns_to_remove = []
        for pattern in self.signal_patterns:
            if (
                len(pattern) == 6
                and pattern.union(self.mappings[1]) == self.mappings[8]
            ):
                self.mappings[6] = pattern
                patterns_to_remove.append(pattern)
        for pattern in patterns_to_remove:
            self.signal_patterns.remove(pattern)

    def find_zero_and_nine(self):
        patterns_to_remove = []
        for pattern in self.signal_patterns:
            if len(pattern) == 6:
                if pattern.union(self.mappings[4]) == self.mappings[8]:
                    self.mappings[0] = pattern
                    patterns_to_remove.append(pattern)
                else:
                    self.mappings[9] = pattern
                    patterns_to_remove.append(pattern)

        for pattern in patterns_to_remove:
            self.signal_patterns.remove(pattern)

    def find_more(self):
        # remaining: 2, 3, 5
        patterns_to_remove = []
        for pattern in self.signal_patterns:
            if pattern.union(self.mappings[1]) == pattern:
                self.mappings[3] = pattern
                patterns_to_remove.append(pattern)
            elif pattern.union(self.mappings[1]) == self.mappings[9]:
                self.mappings[5] = pattern
                patterns_to_remove.append(pattern)
            else:
                self.mappings[2] = pattern
                patterns_to_remove.append(pattern)

        for pattern in patterns_to_remove:
            self.signal_patterns.remove(pattern)

    def resolve_output(self):
        self.find_unique_patterns()
        self.find_six()
        self.find_zero_and_nine()
        self.find_more()

        inverted_mappings = {frozenset(v): k for k, v in self.mappings.items()}

        digits = [inverted_mappings[frozenset(s)] for s in self.outputs]
        return int("".join([str(d) for d in digits]))

    def __repr__(self):
        return f"Signal(patterns: {self.signal_patterns}, mappings: {self.mappings})"


def read_input_string(line):
    return Signal.parse(line)


def read_input(path):
    with open(path) as f:
        for line in f:
            yield read_input_string(line)


def has_unique_segment_count(value):
    # segment counts, not number mappings
    return len(value) in {2, 3, 4, 7}


def part_one(path):
    result = 0
    for signal in read_input(path):
        result += len([o for o in signal.outputs if has_unique_segment_count(o)])
    return result


def part_two(path):
    result = 0
    for signal in read_input(path):
        result += signal.resolve_output()
    return result


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
