# -*- coding: utf-8 -*-
from itertools import product
import random


def init_all_cards():
    suits = '♣♦♠♥'
    numbers = list(range(1, 14))
    return ["{0}{1}".format(suit, number) for suit, number in product(suits, numbers)]


def get_legal_moves(cards_you_have, cards_played, heart_broken=False):
    if cards_played:
        suit = cards_played[0][0]
        card ><
        cards_you_can_play = [card for card in cards_you_have if card.startswith(suit)]
        if cards_you_can_play:
            return cards_you_can_play
        else:
            return cards_you_have
    else:
        if heart_broken:
            return cards_you_have
        else:
            cards_you_can_play = [card for card in cards_you_have if not card.startswith('♥')]
            if cards_you_can_play:
                return cards_you_can_play
            else:
                return cards_you_have


def compute_score(cards):
    score = sum(1 for card in cards if card.startswith('♥'))
    if '♠12' in cards:
        score += 13
    return score


def get_good_moves(cards_you_have, cards_played, heart_broken=False):
    candidates = get_legal_moves(cards_you_have, cards_played, heart_broken)
    if cards_played:
        suit = cards_played[0][0]
        all_numbers = [int(card[1:]) for card in cards_played if card.startswith(suit)]
        max_number = 1 if 1 in all_numbers else max(all_numbers)

        card_score = {}
        for card in candidates:
            card_num = int(card[1:])
            if card.startswith(suit) and ((max_number != 1 and card_num > max_number) or card_num == 1):
                score = compute_score(cards_played + [card])
            else:
                score = 0
            card_score[card] = score
        min_score = min(card_score.values())
        return [card for card in candidates if card_score[card] == min_score]
    else:
        card_score = {}
        for card in candidates:
            card_num = int(card[1:])
            score = compute_score(cards_played + [card])
            card_score[card] = score
        min_score = min(card_score.values())
        return [card for card in candidates if card_score[card] == min_score]


def random_cards(cards):
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
    cards = init_all_cards()
    cards.remove('♣2')
    for _ in range(10):
        cards_you_have, cards_played, heart_broken = random_cards(cards)
        print("You have:", ', '.join(cards_you_have))
        print("Cards played:", cards_played, heart_broken)

        cards_you_can_play = get_legal_moves(cards_you_have, cards_played, heart_broken)
        cards_you_should_play = get_good_moves(cards_you_have, cards_played, heart_broken)
        print("You can play:", ', '.join(cards_you_can_play))
        print("You should play:", ', '.join(cards_you_should_play))

        print()
