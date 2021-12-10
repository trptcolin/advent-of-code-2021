import inspect
import tempfile
import solution

example_input = inspect.cleandoc(
    """[({(<(())[]>[[{[]{<()<>>
           [(()[<>])]({[<{<<[]>>(
           {([(<{}[<>[]}>{[]{[(<()>
           (((({<>}<{<{<>}{[]{[]{}
           [[<[([]))<([[{}[[()]]]
           [{[{({}]{}}([{[{{{}}([]
           {<[[]]>}<{[{[{[]{()[[[]
           [<(<(<(<{}))><([]([]()
           <{([([[(<>()){}]>(<<{{
           <{([{{}}[<[[[<>{}]]]>[]]"""
)


def test_part_one():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        assert solution.part_one(f.name) == 26397


def test_find_error():
    e = solution.find_error("{([(<{}[<>[]}>{[]{[(<()>")
    assert e == solution.Error("]", "}")

    e = solution.find_error("[[<[([]))<([[{}[[()]]]")
    assert e == solution.Error("]", ")")

    e = solution.find_error("[{[{({}]{}}([{[{{{}}([]")
    assert e == solution.Error(")", "]")

    e = solution.find_error("[<(<(<(<{}))><([]([]()")
    assert e == solution.Error(">", ")")

    e = solution.find_error("<{([([[(<>()){}]>(<<{{")
    assert e == solution.Error("]", ">")
