import itertools
import re

player_start_re = re.compile(r"Player (\d+) starting position: (\d+)")


class Player:
    def __init__(self, player_id, start_position):
        self.player_id = player_id
        self.position = start_position % 10
        self.score = 0

    def __repr__(self):
        return (
            f"Player(id:{self.player_id},position:{self.position},score:{self.score})"
        )


def read_input(path):
    with open(path) as f:
        for line in f:
            match = re.match(player_start_re, line)
            player_id, start_position = match.groups()
            yield Player(int(player_id), int(start_position))


def play(players):
    roll_count = 0
    die_rolls = itertools.cycle(range(1, 101))
    while True:
        for player in players:
            roll_total = sum(itertools.islice(die_rolls, 3))
            roll_count += 3
            new_position = (player.position + roll_total) % 10
            player.position = new_position
            if new_position == 0:
                player.score += 10
            else:
                player.score += new_position
            if player.score >= 1000:
                return players, roll_count


def part_one(path):
    players = read_input(path)
    players, roll_count = play(itertools.cycle(players))
    players = list(itertools.islice(players, 2))
    return min([player.score for player in players]) * roll_count


def part_two(path):
    pass


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
