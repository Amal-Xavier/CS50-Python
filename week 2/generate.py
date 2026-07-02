import random

cards = ["jack","queen","king"]
random.shuffle(cards)
for card in range(len(cards)):
    print(f"{card+1} {cards[card]}")