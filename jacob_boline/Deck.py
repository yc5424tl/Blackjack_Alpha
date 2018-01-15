from jacob_boline import Card
import random


class Deck:

    def __init__(self):
        cards = []
        for suit in Card.Suits:
            for rank in Card.Ranks:
                card = Card.Card(suit, rank)
                # print(card.__str__())
                # print(card.get_rank())
                # print(card.get_suit())
                cards.append(card)
        self.cards_in_deck = cards

    def __str__(self):

        print("This deck contains: \n")
        for card in self.cards_in_deck:
            print(card.__str__())
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



