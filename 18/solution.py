import functools
import json


class SnailfishPair:
    def __init__(self, left, right, depth):
        self.left = left
        self.right = right
        self.depth = depth
        self.parent = None

    def __eq__(self, other):
        if other == None or not isinstance(other, SnailfishPair):
            return False
        return self.left == other.left and self.right == other.right

    def __repr__(self):
        return f"SnailfishPair({self.left},{self.right})"

    def explode(self):
        if self.depth >= 4:
            number_to_left = self.find_number_to_left(self.left)
            number_to_right = self.find_number_to_right(self.right)
            if number_to_left:
                number_to_left.value += self.left.value
            if number_to_right:
                number_to_right.value += self.right.value

            v = SnailfishValue(0, self.depth)
            v.parent = self.parent
            if self.parent.left is self:
                self.parent.left = v
            elif self.parent.right is self:
                self.parent.right = v
            return self
        else:
            left_exploded = self.left.explode()
            if left_exploded:
                return left_exploded
            else:
                return self.right.explode()

    def split(self):
        left_split = self.left.split()
        if left_split:
            return left_split
        else:
            return self.right.split()

    def find_number_to_left(self, value):
        prev_parent = self
        parent = self.parent
        while parent != None:
            if parent.left is prev_parent:
                prev_parent = parent
                parent = parent.parent
            else:
                node = parent.left
                while hasattr(node, "right"):
                    node = node.right
                if not hasattr(node, "right"):
                    return node
        return None

    def find_number_to_right(self, value):
        prev_parent = self
        parent = self.parent
        while parent != None:
            if parent.right is prev_parent:
                prev_parent = parent
                parent = parent.parent
            else:
                node = parent.right
                while hasattr(node, "left"):
                    node = node.left
                if not hasattr(node, "left"):
                    return node
        return None

    def reduce(self):
        while True:
            exploded = self.explode()
            if exploded:
                continue
            split = self.split()
            if split:
                continue
            return

    def add(self, other):
        new_top_pair = SnailfishPair(self, other, depth=0)
        self.parent = new_top_pair
        other.parent = new_top_pair
        self.increment_depth()
        other.increment_depth()
        new_top_pair.reduce()
        return new_top_pair

    def increment_depth(self):
        self.depth += 1
        self.left.increment_depth()
        self.right.increment_depth()

    def magnitude(self):
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def __str__(self):
        return f"[{self.left},{self.right}]"

    def copy(self):
        pair = SnailfishPair(self.left.copy(), self.right.copy(), self.depth)
        pair.parent = self.parent
        return pair


class SnailfishValue:
    def __init__(self, value, depth):
        self.value = value
        self.depth = depth
        self.parent = None

    def __eq__(self, other):
        if other == None or not isinstance(other, SnailfishValue):
            return False
        return self.value == other.value

    def __repr__(self):
        return f"v({self.value}, d={self.depth})"

    def explode(self):
        pass

    def split(self):
        if self.value < 10:
            return

        a, b = divmod(self.value, 2)
        pair = SnailfishPair(
            SnailfishValue(a, self.depth + 1),
            SnailfishValue(a + b, self.depth + 1),
            self.depth,
        )
        pair.parent = self.parent
        pair.left.parent = pair
        pair.right.parent = pair
        if self.parent.left is self:
            self.parent.left = pair
        elif self.parent.right is self:
            self.parent.right = pair
        return self

    def increment_depth(self):
        self.depth += 1

    def magnitude(self):
        return self.value

    def __str__(self):
        return f"{self.value}"

    def copy(self):
        node = SnailfishValue(self.value, self.depth)
        node.parent = self.parent
        return node


def make_snailfish_number(xs, depth=0):
    if isinstance(xs, int):
        return SnailfishValue(xs, depth)
    a, b = xs
    left = make_snailfish_number(a, depth + 1)
    right = make_snailfish_number(b, depth + 1)
    pair = SnailfishPair(left, right, depth)
    left.parent = pair
    right.parent = pair
    return pair


def read_input_values(path):
    with open(path) as f:
        for line in f:
            values = json.loads(line)
            yield values


def read_input(path):
    for values in read_input_values(path):
        yield make_snailfish_number(values)


def sum_list(pairs):
    return functools.reduce(lambda x, y: x.add(y), pairs)


def part_one(path):
    pairs = read_input(path)
    result = sum_list(pairs)
    return result.magnitude()


def part_two(path):
    pairs = list(read_input_values(path))
    max_so_far = 0
    for a in pairs:
        for b in pairs:
            if a is not b:
                x, y = make_snailfish_number(a), make_snailfish_number(b)
                sum_pair = x.add(y)
                this_magnitude = sum_pair.magnitude()
                if this_magnitude > max_so_far:
                    max_so_far = this_magnitude
    return max_so_far


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
