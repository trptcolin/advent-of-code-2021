class Population:
    def __init__(self, fishes):
        self.fishes = set(fishes)
        self.size = len(fishes)

    def advance_day(self):
        added_fishes = set()
        for fish in self.fishes:
            new_fish = fish.advance_day()
            if new_fish != None:
                added_fishes.add(new_fish)
                self.size += 1
        self.fishes.update(added_fishes)

    def __repr__(self):
        return f"{[f.timer for f in self.fishes]}"


class Fish:
    def __init__(self, timer):
        self.timer = timer

    def advance_day(self):
        if self.timer == 0:
            self.timer = 6
            return Fish(8)
        else:
            self.timer -= 1
            return None


def read_input(path):
    with open(path) as f:
        line = next(f)
        fish_timers = [int(x) for x in line.split(",")]
        fishes = [Fish(timer) for timer in fish_timers]
        return Population(fishes)


def part_one(path, days):
    population = read_input(path)
    for i in range(days):
        population.advance_day()
    return population.size


def part_two(path, days):
    return part_one(path, days)


if __name__ == "__main__":
    print(part_one("input.txt", 80))
    # print(part_two("input.txt", 256))
