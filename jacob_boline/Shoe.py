# percentage of cards that are dealt sometimes called the 'penetration'
# typically 2, 4, 6, or 8 decks
# when card cut is drawn it indicates that the current game is the last one before a new shuffle

from jacob_boline import Deck, Card


class Shoe:

    def __init__(self):
        decks = 0
        burn = []
        cards = []
        self.number_of_decks = decks
        self.cards_in_shoe = cards
        self.discard_pile = burn

    def __str__(self):
        print("Cards in shoe: \n")
        for card in self.cards_in_shoe:
            print(card.__str__())

    def add_deck(self, deck):
        while len(deck.cards_in_deck) > 0:
            self.cards_in_shoe.append(deck.deal_card())
        self.number_of_decks += 1

    def remove_burn_card(self):
        # assert len(self.cards_in_shoe) == self.number_of_decks * 52
        # print('len = ' + str(len(self.cards_in_shoe)))
        # burn = self.cards_in_shoe.pop(0)
        # print('len after burn = ' + str(len(self.cards_in_shoe)))
        # return burn
        # print("shoe size: " + str(len(self.cards_in_shoe)))
        card_removed = self.cards_in_shoe.pop(0)
        self.discard_pile.append(card_removed)

    def deal_card(self):
            return self.cards_in_shoe.pop(0)

    def show_burn_card(self):
        # print("discard size: " + str(len(self.discard_pile)))
        burn_card = self.discard_pile.pop(0)
        print("Burn Card: " + str(burn_card))
        self.discard_pile.append(burn_card)
        # print("discard size after show burn: " + str(len(self.discard_pile)))
        # print("shoe size: " + str(len(self.cards_in_shoe)))
