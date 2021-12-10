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


def test_completing_an_incomplete_line():
    line = "[({(<(())[]>[[{[]{<()<>>"
    e = solution.find_error(line)
    assert e == solution.Incomplete(line, list("[({([[{{"))
    assert e.autocomplete() == "}}]])})]"


def test_completion_score():
    assert solution.completion_score("])}>") == 294
    assert solution.completion_score("}}>}>))))") == 1480781


def test_part_two():
    with tempfile.NamedTemporaryFile() as f:
        f.write(bytes(example_input, "UTF-8"))
        f.seek(0)

        assert solution.part_two(f.name) == 288957
