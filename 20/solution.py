TRANSLATE = {".": "0", "#": "1"}


def read_input(path):
    with open(path) as f:
        algorithm = next(f).strip()
        next(f)  # empty divider line
        input_image = []
        for line in f:
            input_image.append(line.strip())
        return algorithm, input_image


def neighbor_pixels(location):
    x, y = location
    return [(i, j) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2)]


def value_for_image(input_image, x, y, default):
    if x < 0 or y < 0 or x >= len(input_image) or y >= len(input_image[0]):
        return TRANSLATE[default]

    value = input_image[x][y]
    return TRANSLATE[value]


def make_number(values):
    return int("".join(values), base=2)


def resolve_pixel_to_index(input_image, location, default):
    neighbors = neighbor_pixels(location)
    values = [value_for_image(input_image, x, y, default) for x, y in neighbors]
    return make_number(values)


def enhance_image(input_image, enhancement_algorithm, default):
    height = len(input_image)
    width = len(input_image[0])

    infinite_replacement = enhancement_algorithm[make_number(TRANSLATE[default] * 9)]

    output_image = [
        [infinite_replacement for j in range(width + 2)] for i in range(height + 2)
    ]

    for i in range(len(output_image)):
        for j in range(len(output_image[0])):
            index = resolve_pixel_to_index(input_image, (i - 1, j - 1), default)
            value = enhancement_algorithm[index]
            output_image[i][j] = value

    return output_image, infinite_replacement


def print_image(image):
    print("\n".join(["".join(line) for line in image]))


def part_one(path):
    enhancement_algorithm, input_image = read_input(path)
    replacement = "."
    # print_image(input_image)
    output_image, replacement = enhance_image(
        input_image, enhancement_algorithm, replacement
    )
    # print_image(output_image)
    output_image, replacement = enhance_image(
        output_image, enhancement_algorithm, replacement
    )
    # print_image(output_image)
    return len([c for line in output_image for c in line if c == "#"])


def part_two(path):
    pass


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
