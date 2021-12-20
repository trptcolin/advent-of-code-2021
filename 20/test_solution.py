import tempfile
import solution


def test_part_one():
    enhancement_algorithm, input_image = solution.read_input("example_input.txt")
    assert len(enhancement_algorithm) == 512
    assert len(input_image) == 5
    assert len(input_image[0]) == 5


def test_neighbor_pixels():
    assert solution.neighbor_pixels((5, 10)) == [
        (4, 9),
        (4, 10),
        (4, 11),
        (5, 9),
        (5, 10),
        (5, 11),
        (6, 9),
        (6, 10),
        (6, 11),
    ]


def test_resolve_pixels_to_output_value():
    enhancement_algorithm, input_image = solution.read_input("example_input.txt")

    assert solution.resolve_pixel_to_index(input_image, (2, 2), ".") == 34

    assert solution.resolve_pixel_to_index(input_image, (0, 0), ".") == 18

    assert solution.resolve_pixel_to_index(input_image, (0, 1), ".") == 36
    assert solution.resolve_pixel_to_index(input_image, (0, 2), ".") == 8
    assert solution.resolve_pixel_to_index(input_image, (0, 3), ".") == 16


def test_part_one():
    assert solution.part_one("example_input.txt") == 35
