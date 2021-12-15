import collections
import re


insertion_rule_regex = re.compile(r"(\w\w) -> (\w)")


class Polymer:
    def __init__(self, template, rules):
        self.template = template
        self.rules = rules

    def advance(self):
        pairs = ["".join(pair) for pair in zip(self.template, self.template[1:])]
        # make sure to preserve the last character of the string since we later
        # drop the last of each pair to avoid duplicating pair elements
        pairs.append(f"{self.template[-1]} ")
        result_strings = []
        for pair in pairs:
            if pair in self.rules:
                a, b = pair
                insertion = self.rules[pair]
                result_strings.append(f"{a}{insertion}{b}")
            else:
                result_strings.append(pair)
        self.template = "".join([s[:-1] for s in result_strings])

    def element_counts(self):
        return collections.Counter(self.template)


def read_input(path):
    template = ""
    rules = {}
    with open(path) as f:
        template = next(f).strip()
        for line in f:
            m = insertion_rule_regex.match(line)
            if m:
                pair, to_insert = m.groups()
                rules[pair] = to_insert
            else:
                pass
    return Polymer(template, rules)


def part_one(path):
    polymer = read_input(path)
    for _ in range(10):
        polymer.advance()
    counter = polymer.element_counts()
    ordered_counts = counter.most_common()
    a, most_common = ordered_counts[0]
    z, least_common = ordered_counts[-1]
    return most_common - least_common


def part_two(path):
    pass


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
