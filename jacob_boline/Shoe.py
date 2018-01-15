# percentage of cards that are dealt sometimes called the 'penetration'
# typically 2, 4, 6, or 8 decks
# when card cut is drawn it indicates that the current game is the last one before a new shuffle

from jacob_boline import Deck, Card


class Shoe:

    def __init__(self):
        self.number_of_decks = 0
        self.cards_in_shoe = []
        self.discard_pile = []

    def __str__(self):
        print("Cards in shoe: \n")
        for card in self.cards_in_shoe:
            print(Card.Card.__str__(card))

    def remove_burn_card(self):
        # assert len(self.cards_in_shoe) == self.number_of_decks * 52
        card_removed = self.cards_in_shoe.pop(0)
        self.discard_pile.append(card_removed)

    def deal_card(self):
            return self.cards_in_shoe.pop(0)

    def show_burn_card(self):
        burn_card = self.discard_pile.pop(0)
        print("Burn Card: " + Card.Card.__str__(burn_card))
        self.discard_pile.append(burn_card)
