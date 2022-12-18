from rockfall.bitwise_rocks import Chamber, Rockfall
from rockfall.jets import read_jet_pattern
from rockfall.patterndetection import predict_height

with open('jet_pattern.txt') as file:
    jet_pattern = read_jet_pattern(file)
chamber = Chamber(jet_pattern)
rockfall = Rockfall()

for _ in range(0, 2022):
    chamber.drop_rock(rockfall.get_next_rock())

# print(rockfall.rocks_dropped)
# print_chamber(chamber)

print(chamber.get_rock_height())  # 3211

chamber = Chamber(jet_pattern)

predicted_height = predict_height(chamber, len(jet_pattern), 1000000000000)

print(predicted_height)
