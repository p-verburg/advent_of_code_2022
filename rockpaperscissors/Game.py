from enum import IntEnum


class Move(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3


class Outcome(IntEnum):
    Loss = 0
    Draw = 3
    Win = 6


def find_move(their_move, outcome):
    if outcome == Outcome.Draw:
        return their_move

    if outcome == Outcome.Win:
        if their_move == Move.Scissors:
            return Move.Rock
        return their_move + 1
    if outcome == Outcome.Loss:
        if their_move == Move.Rock:
            return Move.Scissors
        return their_move - 1

    return None


def play_moves(our_move, their_move):
    if our_move == Move.Rock and their_move == Move.Scissors:
        return Outcome.Win
    if our_move == Move.Scissors and their_move == Move.Rock:
        return Outcome.Loss

    if our_move > their_move:
        return Outcome.Win
    if our_move < their_move:
        return Outcome.Loss

    return Outcome.Draw


def play_round(game_round):
    return play_moves(game_round.our_move, game_round.their_move)


class Round:
    def __init__(self, our_move, their_move):
        self.our_move = our_move
        self.their_move = their_move

    def score(self):
        return self.our_move + play_round(self)


class Game:
    def __init__(self, rounds):
        self.rounds = rounds

    def score(self):
        total_score = 0
        for game_round in self.rounds:
            total_score += game_round.score()
        return total_score
