from random import random

def flip_coin():
    if random() > 0.5:
        return "Heads"
    else:
        return "Tails"

for i in range(20):
    print(flip_coin())