from rockpaperscissors.Game import Move, Round, Game, Outcome, find_move


def parse_move(code):
    if code == 'A':
        return Move.Rock
    if code == 'B':
        return Move.Paper
    if code == 'C':
        return Move.Scissors
    return None


def parse_outcome(code):
    if code == 'X':
        return Outcome.Loss
    if code == 'Y':
        return Outcome.Draw
    if code == 'Z':
        return Outcome.Win
    return None


def parse_line(line):
    codes = line.split()

    if not codes or len(codes) is not 2:
        return None

    their_move = parse_move(codes[0])
    outcome = parse_outcome(codes[1])

    return Round(find_move(their_move, outcome), their_move)


def read_game_file(path):
    rounds = []

    with open(path) as file:
        for line in file:
            game_round = parse_line(line)
            if game_round:
                rounds.append(game_round)

    return Game(rounds)
