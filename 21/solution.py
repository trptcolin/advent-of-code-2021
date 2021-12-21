import collections
from functools import lru_cache
import itertools
import re

player_start_re = re.compile(r"Player (\d+) starting position: (\d+)")


class Player:
    def __init__(self, player_id, start_position, score=0):
        self.id = player_id
        self.position = start_position % 10
        self.score = score

    def __repr__(self):
        return f"Player(id:{self.id},position:{self.position},score:{self.score})"

    def __hash__(self):
        return hash((self.id, self.position, self.score))

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.position == other.position
            and self.score == other.score
        )


def read_input(path):
    with open(path) as f:
        for line in f:
            match = re.match(player_start_re, line)
            player_id, start_position = match.groups()
            yield Player(int(player_id), int(start_position))


def update_position_and_score(position, roll):
    new_position = (position + roll) % 10
    position = new_position
    if new_position == 0:
        score = 10
    else:
        score = new_position
    return new_position, score


def play(players):
    roll_count = 0
    die_rolls = itertools.cycle(range(1, 101))
    while True:
        for player in players:
            roll_total = sum(itertools.islice(die_rolls, 3))
            roll_count += 3
            position, score = update_position_and_score(player.position, roll_total)
            player.position = position
            player.score += score
            if player.score >= 1000:
                return players, roll_count


@lru_cache(maxsize=None)
def play_dirac(player_1, player_2):
    # base case (most recent player to go was player 2, so no need to check for
    # any player 1 wins)
    if player_2.score >= 21:
        return {player_1.id: 0, player_2.id: 1}

    winner_counts = collections.defaultdict(lambda: 0)

    # all possible rolls - could use range of sums to enumerate possibilities
    # for a given step, but need to examine *all* recursive universes
    # (probability!)
    possible_rolls = [
        x + y + z for x in [1, 2, 3] for y in [1, 2, 3] for z in [1, 2, 3]
    ]
    for roll in possible_rolls:
        new_position, score = update_position_and_score(player_1.position, roll)
        new_score = player_1.score + score

        recursive_winner_counts = play_dirac(
            player_2,
            Player(player_1.id, new_position, new_score),
        )

        winner_counts[player_1.id] += recursive_winner_counts[player_1.id]
        winner_counts[player_2.id] += recursive_winner_counts[player_2.id]

    return winner_counts


def part_one(path):
    players = read_input(path)
    players, roll_count = play(itertools.cycle(players))
    players = list(itertools.islice(players, 2))
    return min([player.score for player in players]) * roll_count


def part_two(path):
    player_1, player_2 = read_input(path)
    win_counts = play_dirac(player_1, player_2)
    return max(win_counts.values())


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
