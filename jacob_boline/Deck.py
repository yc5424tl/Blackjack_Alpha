from jacob_boline import Card
import random


class Deck:

    # Constructs a deck of cards
    def __init__(self):
        self.cards_in_deck = []
        for suit in Card.Suits:
            for rank in Card.Ranks:
                self.cards_in_deck.append(Card.Card(suit, rank))

    # Can use to verify deck build
    def __str__(self):
        count = 1
        for card in self.cards_in_deck:
            print(str(count) +
                  ' Card Rank: ' + card.get_rank() +
                  ' Card Suit: ' + card.get_suit())
            count += 1
        print()

    def shuffle(self):
        random.shuffle(self.cards_in_deck)

    def deal_card(self):
        return self.cards_in_deck.pop(0)

    def __iter__(self):
        return self

    def __next__(self):
        for index in range(len(self.cards_in_deck) - 1):
            yield self.cards_in_deck[index]
