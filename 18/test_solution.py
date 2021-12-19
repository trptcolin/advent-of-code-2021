import inspect
import tempfile
import solution


def test_make_snailfish_number():
    number = solution.make_snailfish_number([[[[[9, 8], 1], 2], 3], 4])
    assert number.depth == 0
    assert number.right.value == 4
    assert number.right.depth == 1
    assert number.right.parent == number
    assert number.left.right.value == 3
    assert number.left.right.depth == 2
    assert number.left.right.parent == number.left
    assert number.left.left.right.value == 2
    assert number.left.left.right.depth == 3
    assert number.left.left.right.parent == number.left.left
    assert number.left.left.left.right.value == 1
    assert number.left.left.left.right.depth == 4
    assert number.left.left.left.right.parent == number.left.left.left
    assert number.left.left.left.left.right.value == 8
    assert number.left.left.left.left.right.depth == 5
    assert number.left.left.left.left.right.parent == number.left.left.left.left
    assert number.left.left.left.left.left.value == 9
    assert number.left.left.left.left.left.depth == 5
    assert number.left.left.left.left.left.parent == number.left.left.left.left


def test_eq():
    number_1 = solution.make_snailfish_number([[[[[9, 8], 1], 2], 3], 4])
    number_2 = solution.make_snailfish_number([[[[[9, 8], 1], 2], 3], 4])
    assert number_1 == number_2


def test_explode_1():
    number = solution.make_snailfish_number([[[[[9, 8], 1], 2], 3], 4])
    number.explode()
    assert number == solution.make_snailfish_number([[[[0, 9], 2], 3], 4])


def test_explode_2():
    number = solution.make_snailfish_number([7, [6, [5, [4, [3, 2]]]]])
    number.explode()
    assert number == solution.make_snailfish_number([7, [6, [5, [7, 0]]]])


def test_explode_3():
    number = solution.make_snailfish_number([[6, [5, [4, [3, 2]]]], 1])
    number.explode()
    assert number == solution.make_snailfish_number([[6, [5, [7, 0]]], 3])


def test_explode_4():
    number = solution.make_snailfish_number(
        [[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]]
    )
    number.explode()
    assert number == solution.make_snailfish_number(
        [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]
    )


def test_explode_5():
    number = solution.make_snailfish_number([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]])
    number.explode()
    assert number == solution.make_snailfish_number(
        [[3, [2, [8, 0]]], [9, [5, [7, 0]]]]
    )


def test_explode_6():
    number = solution.make_snailfish_number(
        [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]]
    )
    number.explode()
    assert number == solution.make_snailfish_number(
        [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]
    )


def test_split_1():
    number = solution.make_snailfish_number([10, 0])
    number.split()
    assert number == solution.make_snailfish_number([[5, 5], 0])


def test_split_2():
    number = solution.make_snailfish_number([[[[0, 7], 4], [15, [0, 13]]], [1, 1]])
    number.split()
    assert number == solution.make_snailfish_number(
        [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]
    )

    number.split()
    assert number == solution.make_snailfish_number(
        [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]]
    )


def test_multistep_reduce():
    number = solution.make_snailfish_number(
        [[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]
    )
    number.reduce()
    assert number == solution.make_snailfish_number(
        [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]
    )


def test_add_numbers_1():
    a = solution.make_snailfish_number([[[[4, 3], 4], 4], [7, [[8, 4], 9]]])
    b = solution.make_snailfish_number([1, 1])
    result = a.add(b)
    assert result == solution.make_snailfish_number(
        [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]
    )


def test_add_numbers_2():
    a = solution.make_snailfish_number(
        [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]]
    )
    b = solution.make_snailfish_number([7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]])
    result = a.add(b)
    assert result == solution.make_snailfish_number(
        [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]]
    )


def test_add_numbers_3():
    a = solution.make_snailfish_number(
        [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]]
    )
    b = solution.make_snailfish_number(
        [[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]]
    )
    result = a.add(b)
    assert result == solution.make_snailfish_number(
        [[[[6, 7], [6, 7]], [[7, 7], [0, 7]]], [[[8, 7], [7, 7]], [[8, 8], [8, 0]]]]
    )


def test_add_numbers_4():
    a = solution.make_snailfish_number(
        [[[[6, 7], [6, 7]], [[7, 7], [0, 7]]], [[[8, 7], [7, 7]], [[8, 8], [8, 0]]]]
    )
    b = solution.make_snailfish_number(
        [[[[2, 4], 7], [6, [0, 5]]], [[[6, 8], [2, 8]], [[2, 1], [4, 5]]]]
    )
    result = a.add(b)
    assert result == solution.make_snailfish_number(
        [[[[7, 0], [7, 7]], [[7, 7], [7, 8]]], [[[7, 7], [8, 8]], [[7, 7], [8, 7]]]]
    )


def test_sum_list_1():
    pair_values = [[1, 1], [2, 2], [3, 3], [4, 4]]
    pairs = [solution.make_snailfish_number(pair) for pair in pair_values]
    sum_pair = solution.sum_list(pairs)
    assert sum_pair == solution.make_snailfish_number(
        [[[[1, 1], [2, 2]], [3, 3]], [4, 4]]
    )


def test_sum_list_2():
    pair_values = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    pairs = [solution.make_snailfish_number(pair) for pair in pair_values]
    sum_pair = solution.sum_list(pairs)
    assert sum_pair == solution.make_snailfish_number(
        [[[[3, 0], [5, 3]], [4, 4]], [5, 5]]
    )


def test_sum_list_3():
    pair_values = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]
    pairs = [solution.make_snailfish_number(pair) for pair in pair_values]
    sum_pair = solution.sum_list(pairs)
    assert sum_pair == solution.make_snailfish_number(
        [[[[5, 0], [7, 4]], [5, 5]], [6, 6]]
    )


def test_sum_list_4():
    example_input = inspect.cleandoc(
        """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
           [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
           [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
           [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
           [7,[5,[[3,8],[1,4]]]]
           [[2,[2,2]],[8,[8,1]]]
           [2,9]
           [1,[[[9,3],9],[[9,0],[0,7]]]]
           [[[5,[7,4]],7],1]
           [[[[4,2],2],6],[8,7]]"""
    )

    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        pairs = solution.read_input(f.name)
        sum_pair = solution.sum_list(pairs)
        assert sum_pair == solution.make_snailfish_number(
            [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]
        )


def test_part_one():
    example_input = inspect.cleandoc(
        """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
           [[[5,[2,8]],4],[5,[[9,9],0]]]
           [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
           [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
           [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
           [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
           [[[[5,4],[7,7]],8],[[8,3],8]]
           [[9,3],[[9,9],[6,[4,9]]]]
           [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
           [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
    )

    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        pairs = solution.read_input(f.name)
        sum_pair = solution.sum_list(pairs)
        assert sum_pair == solution.make_snailfish_number(
            [[[[6, 6], [7, 6]], [[7, 7], [7, 0]]], [[[7, 7], [7, 7]], [[7, 8], [9, 9]]]]
        )
        assert solution.part_one(f.name) == 4140


def test_magnitude():
    number = solution.make_snailfish_number([9, 1])
    assert number.magnitude() == 29
    assert solution.make_snailfish_number([[9, 1], [1, 9]]).magnitude() == 129
    assert solution.make_snailfish_number([[1, 2], [[3, 4], 5]]).magnitude() == 143

    number = solution.make_snailfish_number([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]])
    assert number.magnitude() == 1384

    number = solution.make_snailfish_number([[[[1, 1], [2, 2]], [3, 3]], [4, 4]])
    assert number.magnitude() == 445

    number = solution.make_snailfish_number([[[[3, 0], [5, 3]], [4, 4]], [5, 5]])
    assert number.magnitude() == 791

    number = solution.make_snailfish_number([[[[5, 0], [7, 4]], [5, 5]], [6, 6]])
    assert number.magnitude() == 1137

    number = solution.make_snailfish_number(
        [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]
    )
    assert number.magnitude() == 3488


def test_part_two():
    example_input = inspect.cleandoc(
        """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
           [[[5,[2,8]],4],[5,[[9,9],0]]]
           [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
           [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
           [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
           [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
           [[[[5,4],[7,7]],8],[[8,3],8]]
           [[9,3],[[9,9],[6,[4,9]]]]
           [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
           [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
    )

    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        pairs = solution.read_input(f.name)
        assert solution.part_two(f.name) == 3993
