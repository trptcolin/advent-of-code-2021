import collections
import itertools


def counts(xs):
    counts = []
    for number in xs:
        for i, value in enumerate(number):
            if len(counts) <= i:
                counts.append(collections.Counter({0: 0, 1: 0}))
            counts[i][int(value)] += 1

    return counts


def binary_number_from_intlist(values):
    strings = [str(c[0]) for c in values]
    return int(str.join("", strings), base=2)


def gamma(counts):
    most_common_with_count = [c.most_common()[0] for c in counts]
    return binary_number_from_intlist(most_common_with_count)


def epsilon(counts):
    least_common_with_count = [c.most_common()[-1] for c in counts]
    return binary_number_from_intlist(least_common_with_count)


def read_lines(path):
    with open(path) as f:
        for line in f:
            yield str.strip(line)


def part_one(path):
    numbers = read_lines(path)
    c = counts(numbers)
    return gamma(c) * epsilon(c)


def count_digits_at_position(i, xs):
    c = collections.Counter()
    for x in xs:
        c[x[i]] += 1
    return c


def most_common_digit(i, xs):
    c = count_digits_at_position(i, xs)
    if c["0"] > c["1"]:
        return "0"
    else:
        return "1"


def least_common_digit(i, xs):
    c = count_digits_at_position(i, xs)
    if c["0"] <= c["1"]:
        return "0"
    else:
        return "1"


def updating_rating(f, numbers):
    for i, c in enumerate(numbers):
        if len(numbers) > 1:
            digit = f(i, numbers)
            numbers = [n for n in numbers if n[i] == digit]
    return int(numbers[0], base=2)


def oxygen_generator_rating(numbers):
    return updating_rating(most_common_digit, numbers)


def co2_scrubber_rating(numbers):
    return updating_rating(least_common_digit, numbers)


def part_two(path):
    numbers = list(read_lines(path))
    return oxygen_generator_rating(numbers) * co2_scrubber_rating(numbers)


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
