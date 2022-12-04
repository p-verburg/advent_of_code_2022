from rockpaperscissors.GameFileReader import read_game_file


game = read_game_file('rock_paper_scissors_game.txt')

print(game.score())
