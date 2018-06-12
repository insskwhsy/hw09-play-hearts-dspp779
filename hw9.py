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
        cards_you_can_play = [card for card in cards_you_have if card.startswith(suit)]
        if cards_you_can_play:
            return cards_you_can_play
        else:
            return cards_you_have
    elif '♣2' in cards_you_have:
        return ['♣2']
    else:
        if heart_broken:
            return cards_you_have
        else:
            cards_you_can_play = [card for card in cards_you_have if not card.startswith('♥')]
            if cards_you_can_play:
                return cards_you_can_play
            else:
                return cards_you_have
            
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


def get_good_moves(cards_you_have, cards_played, heart_broken=False):
    _number = {1: 14, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9,
               10: 10, 11: 11, 12: 12, 13: 13}
    candidates = get_legal_moves(cards_you_have, cards_played, heart_broken)
    
    if cards_played:
        suit = cards_played[0][0]
        all_numbers = [int(card[1:]) for card in cards_played if card.startswith(suit)]
        max_number = 1 if 1 in all_numbers else max(all_numbers)
        bad_cards = ['♥1','♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥10','♥11','♥12','♥13','♠12']
        
        if any(bad_card in cards_played for bad_card in bad_cards):
            
            first_good_cards = [card for card in candidates if card.startswith(suit) and _number[int(card[1:])] < max_number ] + [card for card in candidates if not card.startswith(suit) ]               
            second_good_cards = [card for card in candidates if card.startswith(suit) and _number[int(card[1:])] > max_number and card != '♠12']
            third_good_cards = [card for card in candidates if card not in first_good_cards and second_good_cards]
            if first_good_cards : 
                return [card for card in first_good_cards]
            elif second_good_cards:
                return [card for card in second_good_cards]
            else:
                return [card for card in third_good_cards] 
           
        else:
            
            second_good_cards = [card for card in candidates if card.startswith(suit) and card != '♠12' ] + [card for card in candidates if not card.startswith(suit)]
            first_good_cards = [card for card in candidates if card.startswith(suit) ] + [card for card in candidates if not card.startswith(suit)]
            yes_cards = ['♠13','♠1']
            if yes_cards in cards_played:
                return [card for card in first_good_cards]
            else : 
                return [card for card in second_good_cards]
    
            
            
    else:
        return candidates
        
        
        

if __name__ == '__main__':
    cards = init_all_cards()
    cards.remove('♣2')
    for _ in range(10):
        cards_you_have, cards_played, heart_broken = random_cards(cards)
        print("You have:", ', '.join(cards_you_have))
        print("Cards played:", cards_played)

        cards_you_can_play = get_legal_moves(cards_you_have, cards_played, heart_broken)
        cards_you_should_play = get_good_moves(cards_you_have, cards_played, heart_broken)
        print("You can play:", ', '.join(cards_you_can_play))
        print("You should play:", ',' .join(cards_you_should_play))

        print()
