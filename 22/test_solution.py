import solution


def test_example_one():
    assert solution.part_one("example_input_1.txt") == 39


def test_example_two():
    assert solution.part_one("example_input_2.txt") == 590784


def test_example_three():
    assert solution.part_one("example_input_3.txt") == 300


def test_part_two():
    assert solution.part_one("example_input_4.txt") == 474140
    assert solution.part_two("example_input_4.txt") == 2758514936282235
