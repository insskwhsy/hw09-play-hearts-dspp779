# -*- coding: utf-8 -*-
from itertools import product
import random


def init_all_cards():
    suits = '♣♦♠♥'
    numbers = list(range(1, 14))
    return ["{0}{1}".format(suit, number) for suit, number in product(suits, numbers)]


def get_legal_moves(cards_you_have, cards_played, heart_broken=False):
    # write your code ...
    return []


def get_good_moves(cards_you_have, cards_played, heart_broken=False):
    # write your code ...
    return []


def random_cards():
    cards = init_all_cards()
    cards.remove('♣2')
    while True:
        cards_you_have = random.sample(cards, random.choice(range(1, 13)))
        cards_played = random.sample(cards, random.choice(range(4)))

        if any(card.startswith('♥') or card == '♠12' for card in cards_played):
            heart_broken = True
        else:
            heart_broken = random.choice([True, False])

        if all(card not in cards_you_have for card in cards_played):
            return cards_you_have, cards_played, heart_broken


if __name__ == '__main__':
    for _ in range(10):
        cards_you_have, cards_played, heart_broken = random_cards()
        print("You have:", ', '.join(cards_you_have))
        print("Cards played:", cards_played)

        cards_you_can_play = get_legal_moves(cards_you_have, cards_played, heart_broken)
        print("You can play:", ', '.join(cards_you_can_play))

        print()
