import collections


class Population:
    def __init__(self, fish_timers):
        self.size = len(fish_timers)
        self.timer_counts = collections.Counter(fish_timers)

    def advance_day(self):
        # Idea: group by timer.
        # No need to compute the same thing > 1 time, let alone millions,
        # particularly when there are only 9 possible values!
        added_fishes = collections.Counter()
        removed_fishes = collections.Counter()
        for timer in self.timer_counts.copy():
            updated_timer, new_fish = Fish(timer).advance_day()
            count = self.timer_counts[timer]
            removed_fishes[timer] += count
            added_fishes[updated_timer] += count
            if new_fish != None:
                added_fishes[new_fish.timer] += count
                self.size += count
        self.timer_counts.update(added_fishes)
        self.timer_counts.subtract(removed_fishes)

    def __repr__(self):
        return f"{self.timer_counts}"


class Fish:
    def __init__(self, timer):
        self.timer = timer

    def advance_day(self):
        if self.timer == 0:
            self.timer = 6
            return 6, Fish(8)
        else:
            self.timer -= 1
            return self.timer, None


def read_input(path):
    with open(path) as f:
        line = next(f)
        fish_timers = [int(x) for x in line.split(",")]
        return Population(fish_timers)


def part_one(path, days):
    population = read_input(path)
    for i in range(days):
        population.advance_day()
    return population.size


def part_two(path, days):
    return part_one(path, days)


if __name__ == "__main__":
    print(part_one("input.txt", 80))
    print(part_two("input.txt", 256))
